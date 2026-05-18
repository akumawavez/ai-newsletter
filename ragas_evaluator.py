"""RAGAS evaluation for generated newsletter summaries.

Maps each newsletter item to a single-turn RAG evaluation row:

* ``user_input`` — audience-specific summarization instruction (LLM judge task).
* ``retrieved_contexts`` — source fields from the dataset (the "retrieved" context).
* ``response`` — generated ``tech_summary`` or ``nontech_summary``.
* ``reference`` — ``short_summary`` / ``full_summary`` from the dataset.

Metrics (LLM-as-judge unless noted):

**Generation**
  - faithfulness — claims in the response supported by context.
  - answer_relevancy — response addresses the instruction (embeddings + LLM).
  - factual_correctness — alignment with reference summary.

**Retrieval / context**
  - context_precision — retrieved context relevant to the task.
  - context_recall — context covers the reference answer.
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from llm_summarizer import SOURCE_FIELDS


EVAL_DATA_DIR = Path("data")
EVAL_CACHE_DIR = EVAL_DATA_DIR / "ragas_evaluations"

GENERATION_METRICS = ("faithfulness", "answer_relevancy", "factual_correctness(mode=f1)")
RETRIEVAL_METRICS = ("context_precision", "context_recall")

TECH_INSTRUCTION = (
    "Write a concise technical newsletter blurb (35–60 words) for an engineer "
    "audience, using only the provided source material."
)
NONTECH_INSTRUCTION = (
    "Write a concise non-technical newsletter blurb (35–60 words) for a "
    "business audience, using only the provided source material."
)


@dataclass
class NewsletterEvalReport:
    """Aggregated RAGAS scores for one newsletter run."""

    week_label: str = ""
    sample_count: int = 0
    overall: dict[str, float] = field(default_factory=dict)
    generation: dict[str, float] = field(default_factory=dict)
    retrieval: dict[str, float] = field(default_factory=dict)
    rows: list[dict[str, Any]] = field(default_factory=list)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _clean(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def build_source_context(item: dict[str, Any]) -> str:
    """Render allowed source fields as the retrieved context block."""
    lines = []
    for name in SOURCE_FIELDS:
        value = _clean(item.get(name, ""))
        if value:
            lines.append(f"{name}: {value}")
    return "\n".join(lines)


def build_eval_rows(
    items: list[dict[str, Any]],
    *,
    max_items: int | None = None,
) -> list[dict[str, Any]]:
    """Expand processed newsletter items into RAGAS evaluation rows."""
    rows: list[dict[str, Any]] = []
    subset = items[:max_items] if max_items else items

    for item in subset:
        context = build_source_context(item)
        if not context:
            continue

        reference = _clean(item.get("short_summary")) or _clean(
            item.get("full_summary")
        )
        title = _clean(item.get("title")) or "Untitled"
        item_id = _clean(item.get("item_id"))

        audience_specs = (
            ("tech", TECH_INSTRUCTION, _clean(item.get("tech_summary"))),
            ("nontech", NONTECH_INSTRUCTION, _clean(item.get("nontech_summary"))),
        )

        for audience, instruction, response in audience_specs:
            if not response:
                response = _clean(item.get("newsletter_summary"))
            if not response:
                continue

            rows.append(
                {
                    "user_input": instruction,
                    "retrieved_contexts": [context],
                    "response": response,
                    "reference": reference or context,
                    "title": title,
                    "item_id": item_id,
                    "audience": audience,
                    "section": _clean(item.get("section")),
                }
            )

    return rows


def _get_ragas_clients():
    """Build RAGAS LLM and embedding clients from environment."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is required for RAGAS evaluation. Add it to `.env`."
        )

    from openai import OpenAI
    from langchain_openai import OpenAIEmbeddings
    from ragas.embeddings import LangchainEmbeddingsWrapper
    from ragas.llms import llm_factory

    model = os.getenv("RAGAS_LLM_MODEL") or os.getenv("LLM_MODEL", "gpt-4o-mini")
    embed_model = os.getenv(
        "RAGAS_EMBEDDING_MODEL", "text-embedding-3-small"
    )

    client = OpenAI(api_key=api_key)
    llm = llm_factory(model, client=client)
    embeddings = LangchainEmbeddingsWrapper(
        OpenAIEmbeddings(model=embed_model, api_key=api_key)
    )
    return llm, embeddings


def _metric_means(scores_df) -> dict[str, float]:
    means: dict[str, float] = {}
    for col in scores_df.columns:
        if col in {"user_input", "retrieved_contexts", "response", "reference"}:
            continue
        series = scores_df[col]
        if series.dtype.kind in "biufc":
            val = float(series.mean(skipna=True))
            if val == val:  # not NaN
                means[col] = round(val, 4)
    return means


def _split_metric_groups(means: dict[str, float]) -> tuple[dict, dict, dict]:
    generation, retrieval, overall = {}, {}, {}
    for name, value in means.items():
        overall[name] = value
        if name in GENERATION_METRICS or any(
            g in name for g in ("faithfulness", "answer_relevancy", "factual")
        ):
            generation[name] = value
        elif name in RETRIEVAL_METRICS or "context" in name:
            retrieval[name] = value
    return overall, generation, retrieval


def evaluate_newsletter_items(
    items: list[dict[str, Any]],
    *,
    week_label: str = "",
    edition_date: str = "",
    parent_run_id: str | None = None,
    max_items: int | None = 10,
    show_progress: bool = True,
) -> NewsletterEvalReport:
    """Run RAGAS metrics on newsletter summaries."""
    eval_rows = build_eval_rows(items, max_items=max_items)
    if not eval_rows:
        return NewsletterEvalReport(
            week_label=week_label,
            error="No summaries available to evaluate.",
        )

    try:
        from ragas import EvaluationDataset, evaluate
        from ragas.metrics._answer_relevance import answer_relevancy
        from ragas.metrics._context_precision import context_precision
        from ragas.metrics._context_recall import context_recall
        from ragas.metrics._faithfulness import faithfulness
        from ragas.metrics._factual_correctness import FactualCorrectness

        llm, embeddings = _get_ragas_clients()
        ragas_rows = [
            {
                "user_input": r["user_input"],
                "retrieved_contexts": r["retrieved_contexts"],
                "response": r["response"],
                "reference": r["reference"],
            }
            for r in eval_rows
        ]

        dataset = EvaluationDataset.from_list(ragas_rows)
        metrics = [
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall,
            FactualCorrectness(),
        ]

        result = evaluate(
            dataset=dataset,
            metrics=metrics,
            llm=llm,
            embeddings=embeddings,
            show_progress=show_progress,
        )

        scores_df = result.to_pandas()
        meta_cols = ["title", "item_id", "audience", "section"]
        for idx, meta in enumerate(eval_rows):
            for key in meta_cols:
                scores_df.loc[idx, key] = meta[key]

        means = _metric_means(scores_df)
        overall, generation, retrieval = _split_metric_groups(means)

        detail_rows = scores_df.to_dict(orient="records")
        for row in detail_rows:
            for key, val in row.items():
                if isinstance(val, float) and val == val:
                    row[key] = round(val, 4)

        report = NewsletterEvalReport(
            week_label=week_label,
            sample_count=len(eval_rows),
            overall=overall,
            generation=generation,
            retrieval=retrieval,
            rows=detail_rows,
        )

        try:
            from mlflow_tracker import get_active_run_id, log_ragas_report_to_mlflow

            run_id = parent_run_id or get_active_run_id()
            log_ragas_report_to_mlflow(
                report,
                parent_run_id=run_id,
                edition_date=edition_date,
            )
        except Exception:
            pass

        return report

    except Exception as exc:
        return NewsletterEvalReport(
            week_label=week_label,
            sample_count=len(eval_rows),
            error=str(exc),
        )


def save_eval_report(report: NewsletterEvalReport, edition_date: str) -> Path:
    EVAL_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = EVAL_CACHE_DIR / f"ragas_eval_{edition_date}.json"
    path.write_text(
        json.dumps(report.to_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def load_eval_report(edition_date: str) -> NewsletterEvalReport | None:
    path = EVAL_CACHE_DIR / f"ragas_eval_{edition_date}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return NewsletterEvalReport(**data)
    except (json.JSONDecodeError, OSError, TypeError):
        return None


def score_bar(score: float | None) -> str:
    if score is None or score != score:
        return "—"
    pct = int(round(score * 100))
    filled = pct // 10
    return f"{'█' * filled}{'░' * (10 - filled)} {pct}%"


def render_ragas_detail_panel(report: NewsletterEvalReport) -> None:
    """Streamlit panel for direct RAGAS score breakdown."""
    import streamlit as st

    st.markdown("**RAGAS (direct)**")
    st.caption("LLM-as-judge via the RAGAS library; also logged to MLflow.")

    if report.error:
        st.error(report.error)
        return

    if not report.sample_count:
        st.info("No evaluation samples.")
        return

    st.metric("Samples evaluated", report.sample_count)

    def _mean(scores: dict[str, float]) -> float | None:
        vals = [v for v in scores.values() if isinstance(v, (int, float)) and v == v]
        return sum(vals) / len(vals) if vals else None

    gen_mean = _mean(report.generation)
    ret_mean = _mean(report.retrieval)
    if gen_mean is not None:
        st.metric("Generation (avg)", f"{gen_mean:.2f}")
    if ret_mean is not None:
        st.metric("Retrieval / context (avg)", f"{ret_mean:.2f}")

    if report.generation:
        st.markdown("**Generation metrics**")
        for name, value in report.generation.items():
            label = name.replace("_", " ").replace("(mode=f1)", "").strip().title()
            st.progress(min(max(value, 0.0), 1.0), text=f"{label}: {value:.2f}")

    if report.retrieval:
        st.markdown("**Retrieval / context metrics**")
        for name, value in report.retrieval.items():
            label = name.replace("_", " ").title()
            st.progress(min(max(value, 0.0), 1.0), text=f"{label}: {value:.2f}")

    if report.overall:
        with st.expander("Overall metric means"):
            for name, value in sorted(report.overall.items()):
                st.write(f"**{name}:** {value:.3f} ({score_bar(value)})")

    if report.rows:
        with st.expander("Per-item scores"):
            for row in report.rows:
                title = row.get("title", "Untitled")
                audience = row.get("audience", "")
                st.markdown(f"**{title}** · {audience}")
                cols = st.columns(4)
                metrics_show = [
                    ("Faithfulness", "faithfulness"),
                    ("Relevancy", "answer_relevancy"),
                    ("Factual", "factual_correctness(mode=f1)"),
                    ("Ctx recall", "context_recall"),
                ]
                for col, (label, key) in zip(cols, metrics_show):
                    val = row.get(key)
                    if isinstance(val, (int, float)) and val == val:
                        col.metric(label, f"{val:.2f}")
                    else:
                        col.metric(label, "—")
                st.divider()
