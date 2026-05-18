"""Streamlit UI to generate the weekly LLMOps newsletter on demand."""

from __future__ import annotations

import contextlib
import io
from datetime import date
from pathlib import Path

import streamlit as st

from generate_newsletter import fetch_processed_items
from process_analyze import get_week_window
from ragas_evaluator import (
    NewsletterEvalReport,
    evaluate_newsletter_items,
    load_eval_report,
    render_eval_panel,
    save_eval_report,
)


st.set_page_config(
    page_title="LLMOps Newsletter Generator",
    layout="wide",
    initial_sidebar_state="expanded",
)


def capture_stdout(func, *args, **kwargs):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        result = func(*args, **kwargs)
    return result, buffer.getvalue()


st.title("LLMOps Newsletter Generator")
st.caption(
    "Pick any day in the target week, then run ingestion, analysis, and "
    "Markdown generation for that Monday–Sunday window."
)

col_date, col_week = st.columns([1, 2])

with col_date:
    selected_date = st.date_input(
        "Select a date",
        value=date.today(),
        help="Any day in the week you want. The pipeline uses that week's Mon–Sun.",
    )

week_start, week_end = get_week_window(selected_date)

with col_week:
    st.info(
        f"**Target week:** {week_start.strftime('%A %d %b %Y')} (Mon) → "
        f"{week_end.strftime('%A %d %b %Y')} (Sun)"
    )

st.divider()

generate = st.button("Generate newsletter", type="primary", use_container_width=False)

if generate:
    with st.status("Running pipeline…", expanded=True) as status:
        def log_step(label: str):
            st.write(label)

        try:
            log_step("1/3 — Ingesting Hugging Face dataset…")
            from ingest_dataset import ingest

            _, ingest_log = capture_stdout(ingest)
            if ingest_log.strip():
                with st.expander("Ingestion log"):
                    st.code(ingest_log)

            log_step("2/3 — Processing, ranking, and summarizing items…")
            from process_analyze import process_and_analyze

            process_result, process_log = capture_stdout(
                process_and_analyze,
                reference_date=selected_date,
            )
            if process_log.strip():
                with st.expander("Processing log"):
                    st.code(process_log)

            if process_result is None:
                status.update(label="No items for this week", state="error")
                st.error(
                    "No fresh, non-duplicate items matched this week. "
                    "Try another date or clear `data/published_ids.json` if testing."
                )
                st.stop()

            log_step("3/3 — Rendering Markdown newsletter…")
            from generate_newsletter import generate_markdown_newsletter

            output_path, gen_log = capture_stdout(
                generate_markdown_newsletter,
                reference_date=selected_date,
            )
            if gen_log.strip():
                with st.expander("Generation log"):
                    st.code(gen_log)

            status.update(label="Pipeline complete", state="complete")
            st.session_state["last_output_path"] = str(output_path)
            st.session_state["last_week_start"] = week_start.isoformat()
            st.session_state["last_week_end"] = week_end.isoformat()
            st.session_state["last_edition_date"] = week_end.isoformat()
            st.session_state.pop("eval_report", None)
            if run_ragas:
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

        edition_date = st.session_state.get(
            "last_edition_date", week_end.isoformat()
        )
        week_label = (
            f"{st.session_state.get('last_week_start')} – "
            f"{st.session_state.get('last_week_end')}"
        )

        col_news, col_eval = st.columns([3, 2], gap="large")

        with col_news:
            st.subheader("Newsletter preview")
            st.markdown(markdown)

        with col_eval:
            if "eval_report" not in st.session_state:
                cached = load_eval_report(edition_date)
                if cached and not cached.error:
                    st.session_state["eval_report"] = cached

            rerun_eval = st.button("Run / refresh RAGAS evaluation")
            eval_pending = st.session_state.pop("eval_pending", False)

            if rerun_eval or eval_pending:
                try:
                    items = fetch_processed_items()
                    with st.spinner("Running RAGAS evaluation (LLM-as-judge)…"):
                        report = evaluate_newsletter_items(
                            items,
                            week_label=week_label,
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

            report = st.session_state.get("eval_report")
            if report:
                render_eval_panel(report)
            else:
                st.info(
                    "Enable **Run RAGAS evaluation** in the sidebar or click "
                    "**Run / refresh RAGAS evaluation** to score the newsletter."
                )
    else:
        st.warning(f"Expected output file not found: {output_path}")

st.sidebar.markdown("### RAGAS evaluation")
run_ragas = st.sidebar.checkbox(
    "Run RAGAS evaluation after generate",
    value=True,
    help="Scores faithfulness, relevancy, and context metrics via LLM-as-judge.",
)
max_eval_items = st.sidebar.slider(
    "Max items to evaluate",
    min_value=3,
    max_value=25,
    value=10,
    help="Top-ranked items by trending score (each has tech + nontech rows).",
)

st.sidebar.markdown("### Tips")
st.sidebar.markdown(
    "- Set `OPENAI_API_KEY` in `.env` for LLM summaries and RAGAS evals.\n"
    "- Use **Explore dataset** in the sidebar to browse ingested items.\n"
    "- Published item ids are tracked in `data/published_ids.json`."
)
