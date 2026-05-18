"""Streamlit panels for MLflow evaluation and monitoring."""

from __future__ import annotations

from mlflow_tracker import MonitoringSnapshot, fetch_latest_metrics, load_monitoring_snapshot
from ragas_evaluator import NewsletterEvalReport, render_ragas_detail_panel


METRIC_HELP = {
    "faithfulness": (
        "Are the summary sentences supported by the source text? "
        "Higher is better (less hallucination)."
    ),
    "answer_relevancy": (
        "Does the summary answer the specific summarization task for that "
        "article? Higher means it stays on topic."
    ),
    "context_precision": (
        "Is the source context relevant to the task? High scores mean "
        "we fed the model the right material."
    ),
    "context_recall": (
        "Does the source context contain enough information to write the "
        "summary? High scores mean nothing important was missing."
    ),
    "factual_correctness": (
        "How closely does the summary match the reference summary from "
        "the dataset?"
    ),
}

STAGE_LABELS = {
    "ingest": "Load dataset from Hugging Face into SQLite",
    "process_rank_filter": "Filter by week, deduplicate, score, and categorize",
    "llm_summarize": "OpenAI calls — one per item, returns tech + nontech JSON",
    "persist_processed": "Save ranked items to SQLite / JSONL",
    "render_markdown": "Assemble the `.md` newsletter file from SQLite",
}


def _mean(scores: dict[str, float]) -> float | None:
    vals = [v for v in scores.values() if isinstance(v, (int, float)) and v == v]
    return sum(vals) / len(vals) if vals else None


def _filter_metrics(metrics: dict[str, float], prefix: str) -> dict[str, float]:
    return {k: v for k, v in metrics.items() if k.startswith(prefix)}


def _format_duration(seconds: float) -> str:
    if seconds >= 1.0:
        return f"{seconds:.2f}s"
    if seconds >= 0.001:
        return f"{seconds * 1000:.0f}ms"
    return "<1ms"


def _display_metric_group(title: str, metrics: dict[str, float]) -> None:
    import streamlit as st

    if not metrics:
        return
    st.markdown(f"**{title}**")
    for name, value in sorted(metrics.items()):
        label = name.replace("_", " ").replace("ragas ", "").title()
        if name.endswith("_sec") or name.endswith("_ms"):
            if name.endswith("_ms"):
                st.write(f"- {label}: **{value:.0f} ms**")
            else:
                st.write(f"- {label}: **{_format_duration(value)}**")
        elif "token" in name or name.endswith("_calls"):
            st.metric(label, f"{int(value)}")
        else:
            help_text = METRIC_HELP.get(name.split("_")[-1], "")
            st.progress(min(max(value, 0.0), 1.0), text=f"{label}: {value:.3f}")
            if help_text:
                st.caption(help_text)


def render_evaluation_section(
    report: NewsletterEvalReport | None,
    edition_date: str,
) -> None:
    """Evaluation subsection: MLflow-latest metrics + RAGAS detail."""
    import streamlit as st

    st.subheader("Evaluation")
    st.caption(
        "Scores measure summary quality. **Retrieval** = was the right source "
        "material used? **Generation** = was the LLM summary faithful and on-topic?"
    )

    mlflow_data = fetch_latest_metrics(edition_date)
    eval_metrics = mlflow_data.get("evaluation_metrics", {})
    ragas_mlflow = _filter_metrics(eval_metrics, "ragas_")

    if ragas_mlflow:
        st.markdown("**MLflow (latest run)**")
        st.caption(
            f"Run `{mlflow_data.get('evaluation_run_id', '—')}` · "
            "RAGAS metrics stored in MLflow for trend tracking."
        )
        gen = {k: v for k, v in ragas_mlflow.items() if "generation" in k}
        ret = {k: v for k, v in ragas_mlflow.items() if "retrieval" in k}
        core = {
            k: v
            for k, v in ragas_mlflow.items()
            if k not in gen and k not in ret and "generation" not in k and "retrieval" not in k
        }

        gen_mean = _mean(gen) or _mean(core)
        ret_mean = _mean(ret)
        cols = st.columns(2)
        if gen_mean is not None:
            cols[0].metric(
                "Generation (avg)",
                f"{gen_mean:.2f}",
                help="Faithfulness, relevancy, and factual alignment combined.",
            )
        if ret_mean is not None:
            cols[1].metric(
                "Retrieval / context (avg)",
                f"{ret_mean:.2f}",
                help="Whether source context was relevant and complete.",
            )

        _display_metric_group("Generation metrics", gen or core)
        _display_metric_group("Retrieval / context metrics", ret)
    else:
        st.info("No MLflow evaluation metrics yet. Run **Evaluation** after generating.")

    st.divider()

    if report:
        render_ragas_detail_panel(report)
    else:
        st.caption("Run evaluation to populate per-item RAGAS scores.")


def render_monitoring_section(
    edition_date: str,
    snapshot: MonitoringSnapshot | None = None,
) -> None:
    """Monitoring subsection: latency, tokens, throughput from MLflow."""
    import streamlit as st

    st.subheader("Monitoring")
    st.caption(
        "Operational stats for one pipeline run. **LLM calls** = one OpenAI "
        "request per article (each returns both tech and non-technical blurbs)."
    )

    if snapshot is None:
        snapshot = load_monitoring_snapshot(edition_date)

    mlflow_data = fetch_latest_metrics(edition_date)
    pipeline_metrics = mlflow_data.get("pipeline_metrics", {})

    if snapshot is None and not pipeline_metrics:
        st.info("Generate a newsletter to record monitoring metrics.")
        return

    st.caption(
        f"Pipeline run `{mlflow_data.get('pipeline_run_id') or (snapshot.run_id if snapshot else '—')}`"
    )

    llm = snapshot.llm if snapshot else None

    col1, col2, col3 = st.columns(3)
    total_tokens = (
        llm.total_tokens
        if llm
        else int(pipeline_metrics.get("llm_total_tokens", 0))
    )
    avg_latency = (
        llm.avg_latency_sec
        if llm
        else float(pipeline_metrics.get("llm_avg_latency_sec", 0))
    )
    throughput = (
        snapshot.throughput_items_per_min
        if snapshot
        else float(pipeline_metrics.get("throughput_items_per_min", 0))
    )

    items_in = (
        snapshot.items_in_newsletter
        if snapshot
        else int(pipeline_metrics.get("items_in_newsletter", 0))
    )
    llm_calls = llm.calls if llm else int(pipeline_metrics.get("llm_calls", 0))

    col1.metric(
        "Total tokens",
        f"{total_tokens:,}",
        help="All prompt + completion tokens sent to the LLM API this run.",
    )
    col2.metric(
        "Avg LLM latency",
        _format_duration(avg_latency),
        help="Average wall-clock time per OpenAI request (excluding cache hits).",
    )
    col3.metric(
        "Throughput",
        f"{throughput:.1f} items/min",
        help="Newsletter items completed per minute of total pipeline time.",
    )

    col4, col5, col6 = st.columns(3)
    col4.metric(
        "LLM calls",
        llm_calls,
        help=f"Usually equals items in newsletter ({items_in}). One call writes both audience blurbs.",
    )
    col5.metric(
        "Cache hits",
        llm.cache_hits if llm else int(pipeline_metrics.get("llm_cache_hits", 0)),
        help="Summaries reused from `data/llm_summaries_cache.json` (no API call).",
    )
    col6.metric("Items in newsletter", items_in)

    if llm and llm.prompt_tokens:
        prompt_share = 100 * llm.prompt_tokens / max(llm.total_tokens, 1)
        st.caption(
            f"Token mix: **{prompt_share:.0f}%** prompt (source text) · "
            f"**{100 - prompt_share:.0f}%** completion (generated blurbs)."
        )

    if snapshot and snapshot.stages:
        st.markdown("**Stage latency**")
        max_stage = max(s.duration_sec for s in snapshot.stages) or 0.01
        for stage in snapshot.stages:
            label = STAGE_LABELS.get(stage.name, stage.name)
            st.progress(
                min(stage.duration_sec / max_stage, 1.0),
                text=f"{stage.name}: {_format_duration(stage.duration_sec)} — {label}",
            )
    else:
        stage_sec = {
            k.replace("stage_", "").replace("_sec", ""): v
            for k, v in pipeline_metrics.items()
            if k.endswith("_sec") and k.startswith("stage_")
        }
        if stage_sec:
            st.markdown("**Stage latency**")
            for name, sec in stage_sec.items():
                label = STAGE_LABELS.get(name, name)
                st.write(f"- **{name}**: {_format_duration(sec)} — {label}")

    total_sec = float(
        pipeline_metrics.get("pipeline_total_sec", 0)
        or (sum(s.duration_sec for s in snapshot.stages) if snapshot else 0)
    )
    if total_sec:
        st.metric("Total pipeline time", _format_duration(total_sec))
