"""LLM-backed summarization for newsletter items.

Produces two short summaries per dataset row:

* ``tech``    -- engineer-readable, may reference tools/techniques.
* ``nontech`` -- plain language for a business reader.

Strict anti-hallucination policy:

* The prompt is built only from the row's own fields (title, company,
  industry, tags, short/full summary). Nothing from outside the dataset
  is added.
* The system prompt explicitly forbids inventing facts.
* The model is called with ``temperature=0.2`` and JSON mode so the
  output shape is deterministic.
* Any URLs the model tries to insert are stripped post-hoc (the only
  link that ends up in the newsletter is the original ``source_url``).
* Outputs are cached on disk by ``item_id`` so re-runs are free and
  identical wording is reused week-to-week.
"""

import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv


CACHE_PATH = Path("data/llm_summaries_cache.json")

# Inputs the LLM is allowed to see. Everything else (e.g. score, week
# window, internal IDs) is intentionally hidden so it cannot leak into
# the generated text.
SOURCE_FIELDS = (
    "title",
    "company",
    "industry",
    "year",
    "application_tags",
    "tools_tags",
    "techniques_tags",
    "short_summary",
    "full_summary",
)

SYSTEM_PROMPT = (
    "You are a careful editor for an internal AI/LLM newsletter. "
    "You write short, factual blurbs strictly from the source material "
    "the user provides. Rules you must follow:\n"
    "1. Use ONLY facts present in the source. Never add details, examples, "
    "names, numbers, dates, or claims that are not in the source.\n"
    "2. If a fact is unclear or missing, omit it. Never speculate.\n"
    "3. Do not invent URLs, citations, or markdown links.\n"
    "4. Each blurb must be between 35 and 60 words.\n"
    "5. Output ONLY a JSON object with exactly two keys: \"tech\" and "
    "\"nontech\".\n\n"
    "\"tech\": for an engineer reader. May reference tools, techniques, "
    "and architectures named in the source. Concrete and specific.\n"
    "\"nontech\": for a business reader. Plain language, focused on the "
    "use case, the company/industry, and the outcome. Avoid jargon."
)

URL_PATTERN = re.compile(r"https?://\S+")


def _build_user_prompt(item):
    """Render the row's allowed fields as a single prompt block."""
    lines = ["Source material:", ""]

    for field in SOURCE_FIELDS:
        value = item.get(field, "")
        if value is None or str(value).strip() == "":
            continue
        lines.append(f"{field}: {value}")

    lines.append("")
    lines.append("Write the JSON now.")
    return "\n".join(lines)


def _strip_urls(text):
    """Remove any URL the model may have invented (defence in depth)."""
    return URL_PATTERN.sub("", text or "").strip()


def _load_cache():
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def _save_cache(cache):
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _heuristic_fallback(item):
    """Used when the LLM is unavailable.

    Reuses ``short_summary``/``full_summary`` verbatim so we never invent
    content. The same string is returned for both audiences; the renderer
    can still display it.
    """
    base = (item.get("short_summary") or item.get("full_summary") or "").strip()
    if not base:
        base = item.get("title", "").strip()
    return {"tech": base, "nontech": base}


def _client():
    """Lazily build an OpenAI client. Returns ``None`` if no key is set."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    try:
        from openai import OpenAI
    except ImportError:
        return None

    return OpenAI(api_key=api_key)


def _call_model(client, item, model):
    """One LLM round-trip. Returns a dict with ``tech`` and ``nontech``."""
    response = client.chat.completions.create(
        model=model,
        temperature=0.2,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _build_user_prompt(item)},
        ],
    )
    raw = response.choices[0].message.content or "{}"
    parsed = json.loads(raw)

    return {
        "tech": _strip_urls(parsed.get("tech", "")),
        "nontech": _strip_urls(parsed.get("nontech", "")),
    }


def summarize_for_audiences(item, model=None, use_cache=True):
    """Return ``{"tech": str, "nontech": str}`` for one item.

    Order of resolution:

    1. On-disk cache keyed by ``item_id`` (when ``use_cache`` is True).
    2. OpenAI chat call with the strict anti-hallucination prompt.
    3. Heuristic fallback that reuses the source summary verbatim.
    """
    item_id = item.get("item_id", "")
    cache = _load_cache() if use_cache else {}

    if use_cache and item_id and item_id in cache:
        return cache[item_id]

    client = _client()
    if client is None:
        return _heuristic_fallback(item)

    model = model or os.getenv("LLM_MODEL", "gpt-5.4-nano")

    try:
        summaries = _call_model(client, item, model)
    except Exception as exc:
        print(f"LLM call failed for item {item_id or '?'}: {exc}. "
              "Falling back to heuristic summary.")
        return _heuristic_fallback(item)

    if not summaries["tech"] or not summaries["nontech"]:
        return _heuristic_fallback(item)

    if use_cache and item_id:
        cache[item_id] = summaries
        _save_cache(cache)

    return summaries
