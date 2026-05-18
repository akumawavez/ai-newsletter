"""Orchestrate ingest → process → generate for a selected week."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from generate_newsletter import generate_markdown_newsletter
from ingest_dataset import ingest
from process_analyze import get_week_window, process_and_analyze


@dataclass
class PipelineResult:
    week_start: date
    week_end: date
    output_path: Path | None
    item_count: int
    message: str


def run_weekly_pipeline(
    reference_date: date | None = None,
    *,
    top_n: int = 25,
) -> PipelineResult:
    """Run the full newsletter pipeline for the week containing ``reference_date``."""
    week_start, week_end = get_week_window(reference_date)

    ingest()
    process_and_analyze(top_n=top_n, reference_date=reference_date)

    output_path = generate_markdown_newsletter(reference_date=reference_date)

    from generate_newsletter import fetch_processed_items

    items = fetch_processed_items()
    item_count = len(items)

    return PipelineResult(
        week_start=week_start,
        week_end=week_end,
        output_path=output_path,
        item_count=item_count,
        message=f"Generated {item_count} items for {week_start} – {week_end}.",
    )
