"""Render the weekly newsletter from processed items.

The newsletter has two top-level sections, one per audience:

* ``Technical Audience``    -- uses ``tech_summary`` (engineer voice).
* ``Non-Technical Audience`` -- uses ``nontech_summary`` (plain-language).

Within each audience, items are grouped by their topic category
(Research Highlights, Industry News, etc.) for readability.

After a successful render, the ids of the items that ended up in the
newsletter are appended to the dedup state file so they will not be
republished next week (Step 9 of the pipeline).

Run with::

    python generate_newsletter.py
"""

import sqlite3
from collections import defaultdict
from pathlib import Path

from process_analyze import get_week_window, save_published_ids


DB_PATH = Path("data/llmops_database.db")
OUTPUT_DIR = Path("newsletter_outputs")

CATEGORY_ORDER = [
    "Research Highlights",
    "Industry News",
    "Cool Use Cases",
    "Tools & Infrastructure",
    "Other Noteworthy Items",
]

AUDIENCES = [
    {
        "title": "Technical Audience",
        "intro": (
            "Engineering-flavoured roundup: tools, techniques, "
            "architectures, and production patterns from this week's items."
        ),
        "summary_field": "tech_summary",
    },
    {
        "title": "Non-Technical Audience",
        "intro": (
            "Plain-language roundup: what was built, who built it, "
            "and what business outcome it produced."
        ),
        "summary_field": "nontech_summary",
    },
]


DESIRED_COLUMNS = [
    "item_id",
    "title",
    "company",
    "industry",
    "year",
    "source_url",
    "section",
    "trending_score",
    "newsletter_summary",
    "tech_summary",
    "nontech_summary",
]


def fetch_processed_items():
    """Read the ranked items prepared by ``process_analyze.py``.

    The query is built from whichever of :data:`DESIRED_COLUMNS` exist
    in the table at runtime, so an older schema (for instance one that
    pre-dates the audience-specific summaries) still renders cleanly.
    Missing fields default to ``""`` and the renderer falls back to the
    heuristic ``newsletter_summary`` for both audiences.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("PRAGMA table_info(processed_newsletter_items)")
        existing = {row[1] for row in cursor.fetchall()}

        if not existing:
            raise RuntimeError(
                "Table `processed_newsletter_items` is empty or missing. "
                "Run `python process_analyze.py` first."
            )

        select_cols = [c for c in DESIRED_COLUMNS if c in existing]
        order_clause = (
            "ORDER BY trending_score DESC"
            if "trending_score" in existing
            else ""
        )

        query = (
            f"SELECT {', '.join(select_cols)} "
            f"FROM processed_newsletter_items {order_clause}".strip()
        )
        rows = conn.execute(query).fetchall()

    items = []
    for row in rows:
        item = {col: "" for col in DESIRED_COLUMNS}
        for col, value in zip(select_cols, row):
            item[col] = value
        items.append(item)

    missing = [c for c in DESIRED_COLUMNS if c not in existing]
    if missing:
        print(
            f"Note: regenerating with previous data; missing columns "
            f"({', '.join(missing)}) defaulted to empty."
        )

    return items


def group_by_category(items):
    """Bucket items into ``CATEGORY_ORDER`` sections, keeping order."""
    grouped = defaultdict(list)
    for item in items:
        section = item.get("section") or "Other Noteworthy Items"
        grouped[section].append(item)
    return grouped


def render_item(item, summary_field):
    """Render one item block. Falls back to the heuristic summary if the
    audience-specific LLM summary is missing.
    """
    title = item["title"] or "Untitled"
    company = item["company"] or "Unknown company"
    industry = item["industry"] or "Unknown industry"
    source_url = item["source_url"] or ""

    summary = (
        item.get(summary_field)
        or item.get("newsletter_summary")
        or "No summary available."
    )

    block = [
        f"#### {title}",
        "",
        f"**Company:** {company}  ",
        f"**Industry:** {industry}",
        "",
        summary,
        "",
    ]

    if source_url:
        block.extend([f"[Read source]({source_url})", ""])

    block.append("---")
    block.append("")
    return block


def render_audience_section(audience, grouped_items):
    """Render one top-level audience section with all its categories."""
    lines = [
        f"## {audience['title']}",
        "",
        audience["intro"],
        "",
    ]

    for category in CATEGORY_ORDER:
        items = grouped_items.get(category, [])
        if not items:
            continue

        lines.extend([f"### {category}", ""])
        for item in items:
            lines.extend(render_item(item, audience["summary_field"]))

    return lines


def generate_markdown_newsletter(reference_date=None):
    """Produce the weekly newsletter Markdown file.

    Parameters
    ----------
    reference_date : date-like, optional
        Any day in the target week. The edition is dated on that week's
        Sunday and the header shows the full Mon–Sun range.

    Returns
    -------
    pathlib.Path
        Path to the written Markdown file.
    """
    if not DB_PATH.exists():
        raise FileNotFoundError(
            "Database not found. Run `python ingest_dataset.py` and "
            "`python process_analyze.py` first."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    items = fetch_processed_items()
    grouped = group_by_category(items)
    week_start, week_end = get_week_window(reference_date)
    edition_date = week_end.isoformat()

    lines = [
        f"# Weekly LLMOps Newsletter — {edition_date}",
        "",
        f"*Week of {week_start.isoformat()} (Mon) – {week_end.isoformat()} (Sun)*",
        "",
        "A curated, audience-aware roundup of LLMOps case studies, "
        "production patterns, tools, and use cases. The same items appear "
        "below in two voices: one for engineers and one for business "
        "readers.",
        "",
    ]

    for audience in AUDIENCES:
        lines.extend(render_audience_section(audience, grouped))

    lines.extend([
        "## Closing",
        "",
        "Have a use case worth featuring next week? Reply to share it.",
        "",
    ])

    output_path = OUTPUT_DIR / f"llmops_newsletter_{edition_date}.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Newsletter generated: {output_path}")

    # Step 9: Persist Processed Ids
    # Only after the newsletter is safely on disk; failure here logs but
    # does not raise (the newsletter is already published).
    save_published_ids(item.get("item_id", "") for item in items)

    return output_path


if __name__ == "__main__":
    generate_markdown_newsletter()
