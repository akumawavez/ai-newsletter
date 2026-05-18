"""Weekly newsletter pre-processing.

Pipeline stage that turns the raw ingested HF dataset into a small,
ranked, categorized, summarized set of items ready for the newsletter
renderer.

Order of operations (matches the architecture diagram):

    Preprocessing -> Deduplication + Freshness Filtering ->
    Relevance Ranking -> Topic Categorization -> LLM Summarization

Run with::

    python process_analyze.py
"""

import hashlib
import json
import os
import re
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

from llm_summarizer import summarize_for_audiences


DB_PATH = Path("data/llmops_database.db")
OUTPUT_DIR = Path("data")
PROCESSED_JSONL_PATH = OUTPUT_DIR / "processed_newsletter_items.jsonl"

# State file holding ids of items already published in previous newsletters.
# Used by `apply_dedup_filter` to avoid republishing the same item.
PUBLISHED_IDS_PATH = OUTPUT_DIR / "published_ids.json"

# Freshness window (days). Items older than this are dropped before scoring.
# Override via env var, e.g. NEWSLETTER_LOOKBACK_DAYS=30.
DEFAULT_LOOKBACK_DAYS = int(os.getenv("NEWSLETTER_LOOKBACK_DAYS", "7"))


SECTION_RULES = {
    "Research Highlights": [
        "research",
        "paper",
        "benchmark",
        "evaluation",
        "eval",
        "experiment",
        "model",
        "fine-tuning",
        "finetuning",
        "training",
        "rlhf",
        "rag evaluation",
    ],
    "Industry News": [
        "enterprise",
        "production",
        "deployment",
        "platform",
        "company",
        "customer",
        "business",
        "industry",
        "adoption",
        "scale",
        "infrastructure",
    ],
    "Cool Use Cases": [
        "agent",
        "workflow",
        "assistant",
        "copilot",
        "automation",
        "chatbot",
        "search",
        "support",
        "recommendation",
        "knowledge base",
        "use case",
    ],
    "Tools & Infrastructure": [
        "observability",
        "monitoring",
        "orchestration",
        "vector database",
        "embedding",
        "pipeline",
        "mlops",
        "llmops",
        "framework",
        "tool",
        "open source",
        "guardrails",
    ],
}


TRENDING_KEYWORDS = [
    "agent",
    "agents",
    "rag",
    "retrieval",
    "evaluation",
    "eval",
    "guardrails",
    "observability",
    "production",
    "workflow",
    "automation",
    "copilot",
    "multimodal",
    "embedding",
    "vector",
    "fine-tuning",
    "llmops",
    "open source",
]


def _coerce_date(value):
    """Normalize ``value`` to a :class:`datetime.date`."""
    if value is None:
        return datetime.now().date()
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, str):
        return datetime.fromisoformat(value).date()
    return value


def get_week_window(reference_date=None):
    """Return Monday and Sunday for the week containing ``reference_date``.

  If ``reference_date`` is omitted, uses today's local date.
    """
    day = _coerce_date(reference_date)
    monday = day - timedelta(days=day.weekday())
    sunday = monday + timedelta(days=6)
    return monday, sunday


def get_current_week_window():
    """Return Monday–Sunday for the current local week."""
    return get_week_window()


def clean_text(value):
    if value is None:
        return ""

    if pd.isna(value):
        return ""

    return str(value).strip()


def normalize_whitespace(text):
    text = clean_text(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def truncate_words(text, max_words=45):
    text = normalize_whitespace(text)
    words = text.split()

    if len(words) <= max_words:
        return text

    return " ".join(words[:max_words]).rstrip(".,;:") + "..."


def make_item_id(row):
    """Return a stable SHA-1 id for a dataset row.

    The id is used to deduplicate items across weekly runs. We prefer
    ``source_url`` because it is the most reliable unique key, and fall
    back to ``title|company`` when no URL is available. Returns ``""``
    when neither is present (such rows cannot be deduplicated).
    """
    key = clean_text(row.get("source_url", "")).lower()

    if not key:
        title = clean_text(row.get("title", "")).lower()
        company = clean_text(row.get("company", "")).lower()
        key = f"{title}|{company}".strip("|")

    if not key:
        return ""

    return hashlib.sha1(key.encode("utf-8")).hexdigest()


def load_published_ids():
    """Return the set of item ids published in previous runs.

    Reads :data:`PUBLISHED_IDS_PATH`. Returns an empty set if the file
    does not exist yet or cannot be parsed.
    """
    if not PUBLISHED_IDS_PATH.exists():
        return set()

    try:
        return set(json.loads(PUBLISHED_IDS_PATH.read_text(encoding="utf-8")))
    except (json.JSONDecodeError, OSError):
        return set()


def save_published_ids(new_ids):
    """Append item ids to the persisted published-ids state file.

    The new ids are unioned with whatever ``load_published_ids()``
    returns, so calling this twice with the same ids is a no-op.
    Empty ids are skipped — they cannot be deduplicated reliably and
    would only inflate the state file.

    Failures are logged but never raised: a successful newsletter must
    not be undone by a write error on the state file.
    """
    cleaned = {i for i in new_ids if i}
    if not cleaned:
        print("No publishable item ids to persist.")
        return

    merged = sorted(load_published_ids() | cleaned)

    try:
        PUBLISHED_IDS_PATH.parent.mkdir(parents=True, exist_ok=True)
        PUBLISHED_IDS_PATH.write_text(
            json.dumps(merged, indent=2),
            encoding="utf-8",
        )
        print(
            f"Persisted {len(cleaned)} item ids "
            f"(state now holds {len(merged)})."
        )
    except OSError as exc:
        print(f"Warning: could not write {PUBLISHED_IDS_PATH} ({exc}).")


def apply_freshness_filter(df, lookback_days, week_end):
    """Drop items older than ``lookback_days`` before ``week_end``.

    Items with a missing or unparseable ``created_at`` are kept on
    purpose: the upstream HF dataset has gaps in timestamps and
    silently emptying the newsletter would be worse than including
    a few undated items.

    The Hugging Face dataset is a static snapshot rather than a live
    feed, so a strict 7-day window is often empty. When that happens
    we widen the window progressively (30 -> 90 -> 365 days, then no
    cutoff) and log the fallback. This keeps the pipeline runnable on
    any vintage of the snapshot without manual tweaks.
    """
    if "created_at" not in df.columns:
        return df

    df = df.copy()
    df["created_date"] = pd.to_datetime(
        df["created_at"], errors="coerce"
    ).dt.date

    fallback_windows = [lookback_days, 30, 90, 365, None]
    tried = set()

    for window in fallback_windows:
        if window in tried:
            continue
        tried.add(window)

        if window is None:
            keep = pd.Series(True, index=df.index)
            label = "no cutoff"
        else:
            cutoff = week_end - timedelta(days=window)
            keep = df["created_date"].isna() | (df["created_date"] >= cutoff)
            label = f">= {cutoff} ({window}d)"

        if int(keep.sum()) > 0:
            print(f"Freshness filter ({label}): kept {int(keep.sum())} / {len(df)}")
            if window != lookback_days:
                print(f"  (widened from {lookback_days}d because the strict window was empty)")
            return df[keep].copy()

    print("Freshness filter: dataset is empty.")
    return df.iloc[0:0].copy()


def apply_dedup_filter(df, published_ids):
    """Drop items whose id is already in ``published_ids``.

    Adds an ``item_id`` column to the returned DataFrame so downstream
    steps (newsletter generation, persistence) can reuse it.
    """
    df = df.copy()
    df["item_id"] = df.apply(make_item_id, axis=1)

    if not published_ids:
        return df

    keep = ~df["item_id"].isin(published_ids) | (df["item_id"] == "")
    print(
        f"Dedup filter: kept {int(keep.sum())} / {len(df)} "
        f"(state has {len(published_ids)} ids)"
    )
    return df[keep].copy()


def combined_search_text(row):
    fields = [
        "title",
        "company",
        "industry",
        "short_summary",
        "full_summary",
        "application_tags",
        "tools_tags",
        "techniques_tags",
        "extra_tags",
    ]

    return " ".join(clean_text(row.get(field, "")) for field in fields).lower()


def categorize_item(row):
    """
    Rule-based categorization.
    Good enough for GitHub Actions because it does not require an LLM key.
    """

    text = combined_search_text(row)

    section_scores = {}

    for section, keywords in SECTION_RULES.items():
        score = 0

        for keyword in keywords:
            if keyword.lower() in text:
                score += 1

        section_scores[section] = score

    best_section = max(section_scores, key=section_scores.get)

    if section_scores[best_section] == 0:
        return "Other Noteworthy Items"

    return best_section


def compute_trending_score(row, week_start, week_end):
    """
    Heuristic scoring for 'relevance/trending'.

    Since this dataset is not necessarily a live news feed, we infer relevance from:
    - whether created_at is from the current week
    - recent year
    - presence of high-interest LLMOps keywords
    - quality/completeness of summary
    - source URL availability
    """

    score = 0
    text = combined_search_text(row)

    # 1. Current week boost
    created_at = row.get("created_at")

    if created_at:
        try:
            created_date = pd.to_datetime(created_at, errors="coerce").date()

            if week_start <= created_date <= week_end:
                score += 40
            elif created_date >= week_start - timedelta(days=30):
                score += 20
            elif created_date >= week_start - timedelta(days=90):
                score += 10

        except Exception:
            pass

    # 2. Recent year boost
    year = row.get("year")

    try:
        year_int = int(year)
        current_year = datetime.now().year

        if year_int == current_year:
            score += 20
        elif year_int == current_year - 1:
            score += 12
        elif year_int >= current_year - 2:
            score += 6

    except Exception:
        pass

    # 3. Trending keyword boost
    for keyword in TRENDING_KEYWORDS:
        if keyword in text:
            score += 5

    # 4. Summary quality boost
    short_summary = clean_text(row.get("short_summary", ""))
    full_summary = clean_text(row.get("full_summary", ""))

    if len(short_summary.split()) >= 20:
        score += 8

    if len(full_summary.split()) >= 80:
        score += 8

    # 5. Source availability boost
    if clean_text(row.get("source_url", "")):
        score += 5

    # 6. Company and industry metadata boost
    if clean_text(row.get("company", "")):
        score += 3

    if clean_text(row.get("industry", "")):
        score += 3

    return score


def make_newsletter_summary(row):
    """
    Creates concise newsletter-friendly text without calling an LLM.
    You can later replace this with OpenAI/Anthropic if needed.
    """

    title = clean_text(row.get("title", ""))
    company = clean_text(row.get("company", ""))
    industry = clean_text(row.get("industry", ""))
    short_summary = clean_text(row.get("short_summary", ""))
    full_summary = clean_text(row.get("full_summary", ""))
    tools_tags = clean_text(row.get("tools_tags", ""))
    techniques_tags = clean_text(row.get("techniques_tags", ""))

    base_summary = short_summary or full_summary

    concise_summary = truncate_words(base_summary, max_words=45)

    context_bits = []

    if company:
        context_bits.append(company)

    if industry:
        context_bits.append(industry)

    context = " / ".join(context_bits)

    tags = []

    if tools_tags:
        tags.append(f"Tools: {tools_tags}")

    if techniques_tags:
        tags.append(f"Techniques: {techniques_tags}")

    tags_text = " | ".join(tags)

    parts = []

    if context:
        parts.append(f"**{context}**")

    if concise_summary:
        parts.append(concise_summary)
    elif title:
        parts.append(f"A noteworthy LLMOps item: {title}")

    if tags_text:
        parts.append(tags_text)

    return " — ".join(parts)


def add_audience_summaries(df):
    """Attach LLM-generated ``tech_summary`` and ``nontech_summary`` columns.

    For each row in ``df`` we hand the summarizer only the source fields
    from the dataset; the summarizer itself enforces the no-hallucination
    policy and caches results by ``item_id`` to keep re-runs cheap.
    """
    tech, nontech = [], []

    for _, row in df.iterrows():
        item = {
            "item_id": clean_text(row.get("item_id", "")),
            "title": clean_text(row.get("title", "")),
            "company": clean_text(row.get("company", "")),
            "industry": clean_text(row.get("industry", "")),
            "year": clean_text(row.get("year", "")),
            "application_tags": clean_text(row.get("application_tags", "")),
            "tools_tags": clean_text(row.get("tools_tags", "")),
            "techniques_tags": clean_text(row.get("techniques_tags", "")),
            "short_summary": clean_text(row.get("short_summary", "")),
            "full_summary": clean_text(row.get("full_summary", "")),
        }

        result = summarize_for_audiences(item)
        tech.append(result.get("tech", ""))
        nontech.append(result.get("nontech", ""))

    df = df.copy()
    df["tech_summary"] = tech
    df["nontech_summary"] = nontech
    return df


def load_records():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            "Database not found. Run `python ingest_dataset.py` first.")

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(
            "SELECT * FROM llmops_case_studies",
            conn,
        )

    return df


def process_and_analyze(
    top_n=25,
    lookback_days=DEFAULT_LOOKBACK_DAYS,
    reference_date=None,
):
    """Run the weekly pre-processing pipeline.

    Parameters
    ----------
    top_n : int
        Maximum number of items to keep after ranking.
    lookback_days : int
        Freshness window in days. Items whose ``created_at`` is older
        than this are dropped before scoring.
    reference_date : date-like, optional
        Any day in the target week (Mon–Sun). Defaults to today.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_records()
    week_start, week_end = get_week_window(reference_date)

    print(f"Processing records: {len(df)}")
    print(f"Current week window: {week_start} to {week_end}")

    # Step 4: Deduplication + Freshness Filtering
    df = apply_freshness_filter(df, lookback_days, week_end)
    df = apply_dedup_filter(df, load_published_ids())

    if df.empty:
        print("No fresh, non-duplicate items for this run; nothing to write.")
        return None

    df["section"] = df.apply(categorize_item, axis=1)

    df["trending_score"] = df.apply(
        lambda row: compute_trending_score(row, week_start, week_end),
        axis=1,
    )

    df["newsletter_summary"] = df.apply(make_newsletter_summary, axis=1)

    df["week_start"] = str(week_start)
    df["week_end"] = str(week_end)

    # Sort by score, then recent year if available
    sort_cols = ["trending_score"]

    if "year" in df.columns:
        sort_cols.append("year")

    df = df.sort_values(
        by=sort_cols,
        ascending=False,
    )

    processed = df.head(top_n).copy()

    # Step 7: LLM Summarization (audience-specific, anti-hallucination)
    print(f"Generating LLM summaries for top {len(processed)} items...")
    processed = add_audience_summaries(processed)

    with sqlite3.connect(DB_PATH) as conn:
        processed.to_sql(
            "processed_newsletter_items",
            conn,
            if_exists="replace",
            index=False,
        )

    with open(PROCESSED_JSONL_PATH, "w", encoding="utf-8") as f:
        for _, row in processed.iterrows():
            item = {
                "item_id": clean_text(row.get("item_id", "")),
                "title": clean_text(row.get("title", "")),
                "company": clean_text(row.get("company", "")),
                "industry": clean_text(row.get("industry", "")),
                "year": clean_text(row.get("year", "")),
                "source_url": clean_text(row.get("source_url", "")),
                "section": clean_text(row.get("section", "")),
                "trending_score": int(row.get("trending_score", 0)),
                "newsletter_summary": clean_text(row.get("newsletter_summary", "")),
                "tech_summary": clean_text(row.get("tech_summary", "")),
                "nontech_summary": clean_text(row.get("nontech_summary", "")),
                "tools_tags": clean_text(row.get("tools_tags", "")),
                "techniques_tags": clean_text(row.get("techniques_tags", "")),
                "application_tags": clean_text(row.get("application_tags", "")),
            }

            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print("\nProcessing complete.")
    print(f"Processed table: processed_newsletter_items")
    print(f"Processed JSONL: {PROCESSED_JSONL_PATH}")

    print("\nTop items:")
    preview_cols = [
        "title",
        "company",
        "section",
        "trending_score",
    ]

    existing_preview_cols = [
        col for col in preview_cols if col in processed.columns]

    print(processed[existing_preview_cols].head(10).to_string(index=False))

    return processed


if __name__ == "__main__":
    process_and_analyze(top_n=25)
