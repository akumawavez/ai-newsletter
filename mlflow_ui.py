"""Streamlit panels for MLflow evaluation and monitoring."""

from __future__ import annotations

from typing import Any

from mlflow_tracker import MonitoringSnapshot, fetch_latest_metrics, load_monitoring_snapshot
from ragas_evaluator import NewsletterEvalReport, render_ragas_detail_panel


def _mean(scores: dict[str, float]) -> float | None:
    vals = [v for v in scores.values() if isinstance(v, (int, float)) and v == v]
    return sum(vals) / len(vals) if vals else None


def _filter_metrics(metrics: dict[str, float], prefix: str) -> dict[str, float]:
    return {k: v for k, v in metrics.items() if k.startswith(prefix)}


def _display_metric_group(title: str, metrics: dict[str, float]) -> None:
    import streamlit as st

    if not metrics:
        return
    st.markdown(f"**{title}**")
    for name, value in sorted(metrics.items()):
        label = name.replace("_", " ").replace("ragas ", "").title()
        if name.endswith("_sec"):
            st.metric(label, f"{value:.2f}s")
        elif "token" in name or name.endswith("_calls"):
            st.metric(label, f"{int(value)}")
        else:
            st.progress(min(max(value, 0.0), 1.0), text=f"{label}: {value:.3f}")


def render_evaluation_section(
    report: NewsletterEvalReport | None,
    edition_date: str,
) -> None:
    """Evaluation subsection: MLflow-latest metrics + RAGAS detail."""
    import streamlit as st

    st.subheader("Evaluation")
    mlflow_data = fetch_latest_metrics(edition_date)

    eval_metrics = mlflow_data.get("evaluation_metrics", {})
    ragas_mlflow = _filter_metrics(eval_metrics, "ragas_")

    if ragas_mlflow:
        st.markdown("**MLflow (latest run)**")
        st.caption(
            f"Run `{mlflow_data.get('evaluation_run_id', '—')}` · "
            "RAGAS scores logged via MLflow tracking."
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
            cols[0].metric("Generation (MLflow avg)", f"{gen_mean:.2f}")
        if ret_mean is not None:
            cols[1].metric("Retrieval (MLflow avg)", f"{ret_mean:.2f}")

        _display_metric_group("Generation metrics", gen or core)
        _display_metric_group("Retrieval / context metrics", ret)
    else:
        st.info("No MLflow evaluation metrics yet for this edition.")

    st.divider()

    if report:
        render_ragas_detail_panel(report)
    else:
        st.caption("Run evaluation to populate RAGAS detail scores.")


def render_monitoring_section(
    edition_date: str,
    snapshot: MonitoringSnapshot | None = None,
) -> None:
    """Monitoring subsection: latency, tokens, throughput from MLflow."""
    import streamlit as st

    st.subheader("Monitoring")

    if snapshot is None:
        snapshot = load_monitoring_snapshot(edition_date)

    mlflow_data = fetch_latest_metrics(edition_date)
    pipeline_metrics = mlflow_data.get("pipeline_metrics", {})

    if snapshot is None and not pipeline_metrics:
        st.info("Generate a newsletter to record monitoring metrics.")
        return

    st.caption(
        f"Pipeline run `{mlflow_data.get('pipeline_run_id') or snapshot.run_id if snapshot else '—'}`"
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

    col1.metric("Total tokens", f"{total_tokens:,}")
    col2.metric("Avg LLM latency", f"{avg_latency:.2f}s")
    col3.metric("Throughput", f"{throughput:.1f} items/min")

    col4, col5, col6 = st.columns(3)
    col4.metric(
        "LLM calls",
        llm.calls if llm else int(pipeline_metrics.get("llm_calls", 0)),
    )
    col5.metric(
        "Cache hits",
        llm.cache_hits if llm else int(pipeline_metrics.get("llm_cache_hits", 0)),
    )
    col6.metric(
        "Items in newsletter",
        snapshot.items_in_newsletter
        if snapshot
        else int(pipeline_metrics.get("items_in_newsletter", 0)),
    )

    stage_metrics = _filter_metrics(pipeline_metrics, "stage_")
    if snapshot and snapshot.stages:
        st.markdown("**Stage latency**")
        max_stage = max(s.duration_sec for s in snapshot.stages) or 0.01
        for stage in snapshot.stages:
            st.progress(
                min(stage.duration_sec / max_stage, 1.0),
                text=f"{stage.name}: {stage.duration_sec:.1f}s",
            )
    elif stage_metrics:
        _display_metric_group("Stage latency", stage_metrics)

    if llm and llm.calls:
        st.markdown("**Token breakdown**")
        st.write(
            f"Prompt: **{llm.prompt_tokens:,}** · "
            f"Completion: **{llm.completion_tokens:,}** · "
            f"Total: **{llm.total_tokens:,}**"
        )

    total_sec = float(pipeline_metrics.get("pipeline_total_sec", 0))
    if total_sec:
        st.metric("Total pipeline time", f"{total_sec:.1f}s")
