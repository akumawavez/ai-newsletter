"""Streamlit UI to generate the weekly LLMOps newsletter on demand."""

from __future__ import annotations

import contextlib
import io
from datetime import date
from pathlib import Path

import streamlit as st

from generate_newsletter import fetch_processed_items
from mlflow_tracker import (
    configure_mlflow,
    load_monitoring_snapshot,
    pipeline_run,
    set_pipeline_counts,
    track_stage,
)
from mlflow_ui import render_evaluation_section, render_monitoring_section
from process_analyze import get_selectable_date_bounds, get_week_window
from ragas_evaluator import (
    NewsletterEvalReport,
    evaluate_newsletter_items,
    load_eval_report,
    save_eval_report,
)


st.set_page_config(
    page_title="LLMOps Newsletter Generator",
    layout="wide",
    initial_sidebar_state="expanded",
)

configure_mlflow()

st.sidebar.markdown("### Evaluation")
run_eval = st.sidebar.checkbox(
    "Run evaluation after generate",
    value=True,
    help="RAGAS scoring logged to MLflow + shown in the Evaluation panel.",
)
max_eval_items = st.sidebar.slider(
    "Max items to evaluate",
    min_value=3,
    max_value=25,
    value=10,
    help="Top-ranked items (each has tech + nontech rows).",
)
skip_dedup = st.sidebar.checkbox(
    "Include previously published items",
    value=False,
    help="Bypass dedup state so more stories can appear when testing.",
)

st.sidebar.markdown("### Tips")
st.sidebar.markdown(
    "- Set `OPENAI_API_KEY` in `.env` for LLM summaries and evaluation.\n"
    "- MLflow tracking URI: `MLFLOW_TRACKING_URI` (default `sqlite:///data/mlflow.db`).\n"
    "- Use **Explore dataset** in the sidebar to browse ingested items."
)


def capture_stdout(func, *args, **kwargs):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        result = func(*args, **kwargs)
    return result, buffer.getvalue()


st.title("LLMOps Newsletter Generator")
st.caption(
    "Pick an edition date (today at latest). The newsletter covers the "
    "**previous** calendar week (Mon–Sun) before the week of that date."
)

min_selectable, max_selectable = get_selectable_date_bounds()
default_date = min(max_selectable, max(min_selectable, date.today()))

col_date, col_week = st.columns([1, 2])

with col_date:
    selected_date = st.date_input(
        "Edition date",
        value=default_date,
        min_value=min_selectable,
        max_value=max_selectable,
        help=(
            "The newsletter always uses the prior week's Monday–Sunday. "
            f"Selectable from {min_selectable} through today."
        ),
    )

week_start, week_end = get_week_window(selected_date)
edition_date = week_end.isoformat()
week_label = f"{week_start.isoformat()} – {week_end.isoformat()}"

with col_week:
    st.info(
        f"**Newsletter week (prior Mon–Sun):** "
        f"{week_start.strftime('%A %d %b %Y')} → "
        f"{week_end.strftime('%A %d %b %Y')}"
    )
    st.caption(
        f"Edition anchor: {selected_date.strftime('%A %d %b %Y')} · "
        f"Example: picking 19 May → week of 11–17 May."
    )

st.divider()

generate = st.button("Generate newsletter", type="primary", use_container_width=False)

if generate:
    with pipeline_run(
        edition_date=edition_date,
        week_label=week_label,
        anchor_date=selected_date.isoformat(),
    ) as mlflow_run:
        with st.status("Running pipeline…", expanded=True) as status:
            def log_step(label: str):
                st.write(label)

            try:
                log_step("1/3 — Ingesting Hugging Face dataset…")
                from ingest_dataset import ingest

                with track_stage("ingest"):
                    _, ingest_log = capture_stdout(ingest)
                if ingest_log.strip():
                    with st.expander("Ingestion log"):
                        st.code(ingest_log)

                log_step("2/4 — Filtering, ranking, and categorizing…")
                from process_analyze import process_and_analyze

                with track_stage("process_rank_filter"):
                    ranked, process_log = capture_stdout(
                        process_and_analyze,
                        reference_date=selected_date,
                        run_summarization=False,
                        skip_dedup=skip_dedup,
                    )
                if process_log.strip():
                    with st.expander("Ranking log"):
                        st.code(process_log)

                if ranked is None:
                    status.update(label="No items for this week", state="error")
                    st.error(
                        "No items matched this week. Try another edition date, "
                        "enable **Include previously published items**, or "
                        "clear `data/published_ids.json` when testing."
                    )
                    st.stop()

                log_step("3/4 — LLM summarization (tech + nontech per item)…")
                from process_analyze import (
                    persist_processed_items,
                    summarize_processed_items,
                )

                with track_stage("llm_summarize"):
                    process_result, sum_log = capture_stdout(
                        summarize_processed_items,
                        ranked,
                    )
                if sum_log.strip():
                    with st.expander("Summarization log"):
                        st.code(sum_log)

                with track_stage("persist_processed"):
                    capture_stdout(persist_processed_items, process_result)

                log_step("4/4 — Rendering Markdown newsletter…")
                from generate_newsletter import generate_markdown_newsletter

                with track_stage("render_markdown"):
                    output_path, gen_log = capture_stdout(
                        generate_markdown_newsletter,
                        reference_date=selected_date,
                    )
                if gen_log.strip():
                    with st.expander("Generation log"):
                        st.code(gen_log)

                items = fetch_processed_items()
                set_pipeline_counts(
                    processed=len(process_result),
                    in_newsletter=len(items),
                )

                status.update(label="Pipeline complete", state="complete")
                st.session_state["last_output_path"] = str(output_path)
                st.session_state["last_week_start"] = week_start.isoformat()
                st.session_state["last_week_end"] = week_end.isoformat()
                st.session_state["last_edition_date"] = edition_date
                st.session_state.pop("eval_report", None)
                st.session_state.pop("monitoring_snapshot", None)
                st.session_state["mlflow_pipeline_run_id"] = mlflow_run.info.run_id
                st.session_state["monitoring_snapshot"] = load_monitoring_snapshot(
                    edition_date
                )
                if run_eval:
                    st.session_state["eval_pending"] = True

            except Exception as exc:
                status.update(label="Pipeline failed", state="error")
                st.error(str(exc))
                st.stop()

if "last_output_path" in st.session_state:
    output_path = Path(st.session_state["last_output_path"])

    if output_path.exists():
        st.success(
            f"Newsletter saved for week "
            f"{st.session_state.get('last_week_start')} – "
            f"{st.session_state.get('last_week_end')}: `{output_path}`"
        )

        markdown = output_path.read_text(encoding="utf-8")

        st.download_button(
            label="Download Markdown",
            data=markdown,
            file_name=output_path.name,
            mime="text/markdown",
        )

        edition_date = st.session_state.get("last_edition_date", edition_date)
        week_label = (
            f"{st.session_state.get('last_week_start')} – "
            f"{st.session_state.get('last_week_end')}"
        )

        col_news, col_right = st.columns([3, 2], gap="large")

        with col_news:
            st.subheader("Newsletter preview")
            st.markdown(markdown)

        with col_right:
            eval_tab, monitor_tab = st.tabs(["Evaluation", "Monitoring"])

            with eval_tab:
                if "eval_report" not in st.session_state:
                    cached = load_eval_report(edition_date)
                    if cached and not cached.error:
                        st.session_state["eval_report"] = cached

                rerun_eval = st.button("Run / refresh evaluation", key="rerun_eval")

                if rerun_eval or st.session_state.pop("eval_pending", False):
                    try:
                        items = fetch_processed_items()
                        with st.spinner("Running RAGAS evaluation (logged to MLflow)…"):
                            report = evaluate_newsletter_items(
                                items,
                                week_label=week_label,
                                edition_date=edition_date,
                                parent_run_id=st.session_state.get(
                                    "mlflow_pipeline_run_id"
                                ),
                                max_items=max_eval_items,
                                show_progress=False,
                            )
                        st.session_state["eval_report"] = report
                        if not report.error:
                            save_eval_report(report, edition_date)
                    except Exception as exc:
                        st.session_state["eval_report"] = NewsletterEvalReport(
                            week_label=week_label,
                            error=str(exc),
                        )

                render_evaluation_section(
                    st.session_state.get("eval_report"),
                    edition_date,
                )

            with monitor_tab:
                snapshot = st.session_state.get("monitoring_snapshot")
                if snapshot is None:
                    snapshot = load_monitoring_snapshot(edition_date)
                render_monitoring_section(edition_date, snapshot)

    else:
        st.warning(f"Expected output file not found: {output_path}")
