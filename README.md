# AI Weekly Newsletter Generator

An end-to-end pipeline that automatically curates, summarizes, and publishes a **weekly AI/LLM newsletter** for internal distribution. It ingests the [zenml/llmops-database](https://huggingface.co/datasets/zenml/llmops-database) dataset from Hugging Face, filters and ranks items, uses an LLM to write **two audience-specific summaries** per item (engineer-flavoured and plain-language), and renders a polished Markdown newsletter on a weekly schedule.

> Built as the "Automated AI Newsletter Generator" assignment for TelecomXYZ.

---

## Why this project

Keeping up with the AI/LLM space is hard — too many papers, blog posts, and product launches every week. This pipeline gives an organization a low-effort way to:

- **Stay ahead of trends** by surfacing the latest AI developments
- **Discover new use cases** that could inspire internal projects
- **Reduce information overload** through filtering and LLM summarization
- **Reach both audiences** with the same content delivered in two voices

---

## Architecture

The pipeline is split into nine small stages so each one can be tested, swapped, or scheduled independently.

```text
 Hugging Face Dataset (zenml/llmops-database)
                │
                ▼
   [ 1. Dataset             ]   zenml/llmops-database
                │
                ▼
   [ 2. Ingestion Layer     ]   ingest_dataset.py
                │               -> data/llmops_database.parquet
                │               -> data/llmops_database.db   (SQLite)
                │               -> data/llmops_documents.jsonl (RAG-ready)
                ▼
   [ 3. Preprocessing       ]   process_analyze.py: type coercion,
                │                tag normalization, text cleaning
                ▼
   [ 4. Dedup + Freshness   ]   process_analyze.py:
                │                - drop items older than NEWSLETTER_LOOKBACK_DAYS
                │                - drop ids already in data/published_ids.json
                ▼
   [ 5. Relevance Ranking   ]   process_analyze.py: heuristic scoring
                │                (recency, year, trending keywords, summary
                │                 quality, source-url presence, metadata)
                ▼
   [ 6. Topic Categorization]   process_analyze.py: keyword rules ->
                │                Research Highlights / Industry News /
                │                Cool Use Cases / Tools & Infrastructure /
                │                Other Noteworthy Items
                ▼
   [ 7. LLM Summarization   ]   llm_summarizer.py: per-item summaries
                │                for Technical and Non-Technical audiences
                │                (anti-hallucination prompt + JSON mode +
                │                 disk cache by item_id)
                ▼
   [ 8. Markdown Generation ]   generate_newsletter.py
                │                -> newsletter_outputs/llmops_newsletter_<date>.md
                ▼
   [ 9. Persist Processed   ]   save_published_ids() appends item ids to
       Ids                       data/published_ids.json so next week
                                 won't re-publish them.
```

Each row from the dataset includes metadata such as `created_at`, `title`, `industry`, `company`, `source_url`, `application_tags`, `tools_tags`, `techniques_tags`, `short_summary`, and `full_summary`, which the pipeline uses for both filtering and as prompt context.

---

## Project structure

```text
ai-weeklynewsletter-generator/
├── ingest_dataset.py                # Stage 2: load HF dataset -> parquet + sqlite + jsonl
├── process_analyze.py               # Stages 3–6 + step 9: filter, rank, categorize, persist ids
├── llm_summarizer.py                # Stage 7: audience-specific LLM summaries with cache
├── generate_newsletter.py           # Stage 8: render Markdown newsletter
├── ragas_evaluator.py               # RAGAS LLM-as-judge evaluation for summaries
├── mlflow_tracker.py                # MLflow metrics + monitoring for pipeline/eval
├── mlflow_ui.py                     # Streamlit evaluation & monitoring panels
├── app.py                           # Streamlit generator UI (+ RAGAS scores panel)
├── pages/explore.py                 # Streamlit dataset explorer
├── pyproject.toml                   # Project metadata + dependencies
├── uv.lock                          # Pinned dependency lockfile (committed)
├── data/                            # Generated artifacts; only state files are committed
│   ├── llmops_database.db           # gitignored
│   ├── llmops_database.parquet      # gitignored
│   ├── llmops_documents.jsonl       # gitignored
│   ├── processed_newsletter_items.jsonl  # gitignored
│   ├── published_ids.json           # cross-run dedup state (committed)
│   └── llm_summaries_cache.json     # LLM output cache (committed)
├── newsletter_outputs/
│   └── llmops_newsletter_<date>.md  # one Markdown file per weekly run
├── .github/workflows/
│   └── scheduler.yml                # weekly GitHub Actions run
├── AIassistanceLog.md               # log of how AI assistants were used while building this
└── README.md
```

---

## Quickstart

**Prerequisites:** Python 3.10+, [`uv`](https://docs.astral.sh/uv/), an OpenAI API key.

```bash
# 1. Install dependencies into a project-managed venv
uv sync

# 2. Configure secrets
cp .env.example .env        # then set OPENAI_API_KEY (and optionally LLM_MODEL, NEWSLETTER_LOOKBACK_DAYS)

# 3. Run the weekly pipeline (3 stages)
uv run python ingest_dataset.py        # download Hugging Face dataset -> data/
uv run python process_analyze.py       # freshness + dedup + rank + categorize + LLM summarize
uv run python generate_newsletter.py   # render Markdown -> newsletter_outputs/llmops_newsletter_<date>.md

# 4. Launch the Streamlit app (generate + RAGAS evaluation panel)
uv run streamlit run app.py
```

**Main Python dependencies** (see `pyproject.toml` / `uv.lock`): `datasets`, `pandas`, `openai`, `streamlit`, **`ragas`**, **`mlflow`**, `langchain-openai` (embeddings for RAGAS answer relevancy).

**Re-running:** the pipeline is idempotent. `data/published_ids.json` tracks items already published, and `data/llm_summaries_cache.json` caches LLM outputs by item id, so subsequent runs are cheap and skip duplicates automatically.

**Configurable env vars** (all optional except the API key when LLM summaries are wanted):

| Variable | Default | Purpose |
| --- | --- | --- |
| `OPENAI_API_KEY` | — | Required for LLM summaries and RAGAS evaluation. Without it, summaries fall back to a heuristic. |
| `LLM_MODEL` | `gpt-5.4-nano` | Chat model for newsletter summarization. |
| `RAGAS_LLM_MODEL` | same as `LLM_MODEL` | Judge model for RAGAS metrics (faithfulness, context precision, etc.). |
| `RAGAS_EMBEDDING_MODEL` | `text-embedding-3-small` | Embeddings for RAGAS answer relevancy. |
| `MLFLOW_TRACKING_URI` | `sqlite:///data/mlflow.db` | MLflow tracking store for evaluation + monitoring metrics. |
| `NEWSLETTER_LOOKBACK_DAYS` | `7` | Drop items older than this before scoring. Auto-widens to 30 / 90 / 365 days when the strict window is empty (the HF dataset is a static snapshot). |

---

## How each stage works

### 2. Ingestion (`ingest_dataset.py`)

- Loads the Hugging Face dataset via `datasets.load_dataset("zenml/llmops-database")`.
- Selects a stable subset of columns and coerces types (`created_at` → datetime, `year` → `Int64`).
- Normalises list-typed tag fields (`application_tags`, `tools_tags`, `techniques_tags`, `extra_tags`) into clean comma-separated strings.
- Drops rows without a title.
- Builds a `rag_text` field per record — title, company, industry, tags, and summaries glued into one string — ready for embedding or direct LLM use.
- Writes three formats: **Parquet** (analytics), **SQLite** (ad-hoc SQL), and **JSONL** (RAG / vector store ingestion).

### 3–6. Preprocessing, Filtering, Ranking, Categorization (`process_analyze.py`)

- **Preprocessing** — `clean_text`, `normalize_whitespace`, `truncate_words` for safe string handling.
- **Freshness filter** (`apply_freshness_filter`) — drops items older than `NEWSLETTER_LOOKBACK_DAYS`. Because the upstream dataset is a static snapshot, the filter automatically widens (`7 → 30 → 90 → 365 → no cutoff`) until at least one item is kept, and logs the fallback clearly.
- **Deduplication** (`apply_dedup_filter`) — generates a stable SHA-1 `item_id` per row (preferring `source_url`, falling back to `title|company`), then drops any id already present in `data/published_ids.json` from previous runs.
- **Relevance ranking** (`compute_trending_score`) — heuristic score combining recency, year, trending keywords (`agent`, `rag`, `evaluation`, …), summary completeness, source-URL presence, and company/industry metadata. Top-N items survive (default 25).
- **Topic categorization** (`categorize_item`) — keyword rules bucket each item into one of *Research Highlights*, *Industry News*, *Cool Use Cases*, *Tools & Infrastructure*, with an *Other Noteworthy Items* fallback.

### 7. LLM Summarization (`llm_summarizer.py`)

- One module, one public function: `summarize_for_audiences(item) → {"tech": str, "nontech": str}`.
- The model only sees a fixed list of source fields (`SOURCE_FIELDS`) — title, company, industry, tags, short/full summary. Internal fields (scores, ids) are intentionally hidden so they cannot leak into the text.
- **Anti-hallucination is layered**:
  1. Strict system prompt forbids inventing facts, names, numbers, dates, or URLs.
  2. `temperature=0.2` and `response_format={"type": "json_object"}` for deterministic, schema-shaped output.
  3. Post-processing strips any URL the model might still produce.
  4. Length-bounded outputs (35–60 words) keep the model from smuggling in extra claims.
- **Caching** — results are stored in `data/llm_summaries_cache.json` keyed by `item_id`. Re-runs are free, output is identical week-to-week, and the cache is committed so CI runs benefit too.
- **Graceful fallback** — if the API key is missing or the call fails, the summarizer returns the source `short_summary`/`full_summary` verbatim. The newsletter still ships, just without the LLM polish.

### 8. Markdown Generation (`generate_newsletter.py`)

- Reads `processed_newsletter_items` from SQLite. The query is **schema-tolerant**: it inspects `PRAGMA table_info` and only selects columns that exist, so an older table from a previous run still renders (audience summaries fall back to the heuristic `newsletter_summary`).
- Output structure:

  ```text
  # Weekly LLMOps Newsletter — YYYY-MM-DD
  (intro paragraph)

  ## Technical Audience
    ### Research Highlights
      #### <item>  (uses tech_summary)
    ### Industry News
      ...

  ## Non-Technical Audience
    ### Research Highlights
      #### <item>  (uses nontech_summary)
    ...

  ## Closing
  ```

- Same items appear in both audiences with audience-appropriate wording.
- A live sample is at `newsletter_outputs/llmops_newsletter_2026-05-07.md`.

### 9. Persist Processed Ids (`process_analyze.save_published_ids`)

- Called from `generate_newsletter.py` **after** the Markdown file is safely on disk.
- Unions the just-published `item_id`s with the existing `data/published_ids.json` (so re-running is a no-op).
- Failures are logged but never raised — a successful newsletter must not be undone by a state-write error.

---

## Newsletter structure (audience-aware)

The same items appear under two top-level sections, written in different voices, both grounded in the source dataset:

- **Technical Audience** — engineer-readable. May reference tools, techniques, and architectures named in the source. Concrete and specific.
- **Non-Technical Audience** — plain language. Focuses on the company, the use case, and the outcome. Avoids jargon.

Within each audience, items are sub-grouped by the topic categories above for readability.

---

## Automation

A scheduled GitHub Actions workflow lives at `.github/workflows/scheduler.yml`.

- Runs every **Thursday** (cron `56 10 * * THU` UTC), and is also runnable on demand via *workflow_dispatch*.
- Steps: `uv sync` → `ingest_dataset.py` → `process_analyze.py` (with `OPENAI_API_KEY` from repo secrets) → `generate_newsletter.py` → log dedup-state size → commit & push the new newsletter and updated state files (`data/published_ids.json`, `data/llm_summaries_cache.json`).
- Heavy regenerable artifacts (`*.db`, `*.parquet`, raw JSONL) are gitignored, so the repo stays small even after months of weekly runs.

**One-time setup:** add `OPENAI_API_KEY` as a repo secret under *Settings → Secrets and variables → Actions*. Without it the LLM stage silently falls back to the heuristic summarizer.

---

## Design choices

- **Dataset-as-source-of-truth.** The HF dataset is treated as a read-only upstream feed. All transformations are local, deterministic, and reproducible.
- **Three storage formats on purpose.** Parquet for analytics, SQLite for portable ad-hoc SQL during development and as the renderer's input, JSONL for downstream RAG / embedding pipelines.
- **Modular stages.** Each stage is a separate script/module with clear inputs and outputs, so any one of them can be tested or replaced (e.g. swap OpenAI for a local model in `llm_summarizer.py`) without touching the rest.
- **Anti-hallucination by construction, not by audit.** Limit what the LLM sees; constrain its output shape; cache and persist its outputs so they're auditable; provide a non-LLM fallback so the pipeline is robust to API outages.
- **Schema-tolerant renderer.** Lets you regenerate yesterday's newsletter from yesterday's data even after the schema has moved on.
- **Markdown-first output.** Trivial to email, post to Slack/Teams, or publish to an internal wiki.

---

## Roadmap / bonus features

- [x] **Personalization** — separate Technical and Non-Technical audience sections.
- [x] **Anti-hallucination guardrails** for the LLM stage.
- [x] **LLM output caching** to make re-runs free.
- [x] **Cross-run deduplication** via persisted item ids.
- [x] **Scheduled GitHub Actions workflow.**
- [x] **Quality evaluation** — RAGAS metrics (faithfulness, answer relevancy, context precision/recall, factual correctness) in the Streamlit app.
- [ ] **Vector-store-backed retrieval** for "items similar to past hits".
- [ ] **Slack / Teams / email delivery adapter.**
- [ ] **Configurable section taxonomy** via YAML.

---

## Deliverables checklist

- [x] Source code for the pipeline (`ingest_dataset.py`, `process_analyze.py`, `llm_summarizer.py`, `generate_newsletter.py`, `app.py`)
- [x] `README.md` with setup instructions and design explanation
- [x] Sample generated newsletter (`newsletter_outputs/llmops_newsletter_2026-05-07.md`)
- [x] Scheduled workflow (`.github/workflows/scheduler.yml`)
- [x] AI-assistance transparency log (`AIassistanceLog.md`)
- [ ] `.env.example` (template) — easy to derive from the env-var table above
