"""MLflow tracking for newsletter pipeline monitoring and evaluation."""

from __future__ import annotations

import json
import os
import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from ragas_evaluator import NewsletterEvalReport


MONITORING_DIR = Path("data") / "mlflow_snapshots"
EXPERIMENT_NAME = "llmops-newsletter"
RUN_TYPE_PIPELINE = "newsletter_pipeline"
RUN_TYPE_EVALUATION = "newsletter_evaluation"


@dataclass
class StageMetric:
    name: str
    duration_sec: float
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass
class LLMUsageStats:
    calls: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    total_latency_sec: float = 0.0
    cache_hits: int = 0
    errors: int = 0

    @property
    def avg_latency_sec(self) -> float:
        if self.calls == 0:
            return 0.0
        return self.total_latency_sec / self.calls


@dataclass
class MonitoringSnapshot:
    edition_date: str = ""
    week_label: str = ""
    run_id: str = ""
    stages: list[StageMetric] = field(default_factory=list)
    llm: LLMUsageStats = field(default_factory=LLMUsageStats)
    items_processed: int = 0
    items_in_newsletter: int = 0
    throughput_items_per_min: float = 0.0
    recorded_at: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


_active_monitor: MonitoringSnapshot | None = None
_active_run_id: str | None = None


def configure_mlflow() -> str:
    """Set tracking URI and experiment; return the tracking URI."""
    load_dotenv()
    uri = os.getenv("MLFLOW_TRACKING_URI", "sqlite:///data/mlflow.db")
    import mlflow

    mlflow.set_tracking_uri(uri)
    mlflow.set_experiment(EXPERIMENT_NAME)
    return uri


def _sanitize_metric_name(name: str) -> str:
    return (
        name.replace(" ", "_")
        .replace("(", "")
        .replace(")", "")
        .replace("/", "_")
        .lower()
    )


def log_ragas_report_to_mlflow(
    report: NewsletterEvalReport,
    *,
    parent_run_id: str | None = None,
    edition_date: str = "",
) -> str | None:
    """Log RAGAS aggregates as MLflow metrics on an evaluation child run."""
    import mlflow

    configure_mlflow()
    tags = {
        "edition_date": edition_date,
        "week_label": report.week_label,
        "mlflow.runName": f"evaluation_{edition_date or 'latest'}",
    }

    nested = bool(parent_run_id)
    with mlflow.start_run(
        run_name=f"evaluation_{edition_date or datetime.now().date().isoformat()}",
        nested=nested,
        parent_run_id=parent_run_id if nested else None,
        tags=tags,
    ) as run:
        mlflow.set_tag("run_type", RUN_TYPE_EVALUATION)
        mlflow.log_param("eval_sample_count", report.sample_count)

        for group_name, scores in (
            ("ragas", report.overall),
            ("ragas_generation", report.generation),
            ("ragas_retrieval", report.retrieval),
        ):
            for metric_name, value in scores.items():
                if isinstance(value, (int, float)) and value == value:
                    key = f"{group_name}_{_sanitize_metric_name(metric_name)}"
                    mlflow.log_metric(key, float(value))

        if report.rows:
            mlflow.log_dict(
                {"rows": report.rows[:50]},
                artifact_file="ragas/per_item_scores.json",
            )

        return run.info.run_id


def fetch_latest_metrics(
    edition_date: str | None = None,
) -> dict[str, Any]:
    """Return latest MLflow metrics for pipeline + evaluation runs."""
    import mlflow
    from mlflow.tracking import MlflowClient

    configure_mlflow()
    client = MlflowClient()
    experiment = client.get_experiment_by_name(EXPERIMENT_NAME)
    if experiment is None:
        return {}

    filter_parts = []
    if edition_date:
        filter_parts.append(f"tags.edition_date = '{edition_date}'")
    filter_string = " and ".join(filter_parts) if filter_parts else ""

    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        filter_string=filter_string,
        order_by=["start_time DESC"],
        max_results=20,
    )

    pipeline_run = None
    eval_run = None
    for run in runs:
        run_type = run.data.tags.get("run_type", "")
        if run_type == RUN_TYPE_EVALUATION and eval_run is None:
            eval_run = run
        if run_type == RUN_TYPE_PIPELINE and pipeline_run is None:
            pipeline_run = run

    def _metrics_dict(run) -> dict[str, float]:
        if run is None:
            return {}
        out = {}
        for key, value in run.data.metrics.items():
            if isinstance(value, (int, float)) and value == value:
                out[key] = round(float(value), 4)
        return out

    return {
        "pipeline_run_id": pipeline_run.info.run_id if pipeline_run else None,
        "evaluation_run_id": eval_run.info.run_id if eval_run else None,
        "pipeline_metrics": _metrics_dict(pipeline_run),
        "evaluation_metrics": _metrics_dict(eval_run),
    }


@contextmanager
def pipeline_run(
    edition_date: str,
    week_label: str,
    anchor_date: str,
):
    """Open a parent MLflow run for a full newsletter generation."""
    import mlflow

    global _active_monitor, _active_run_id

    configure_mlflow()
    _active_monitor = MonitoringSnapshot(
        edition_date=edition_date,
        week_label=week_label,
        recorded_at=datetime.now().isoformat(),
    )

    with mlflow.start_run(
        run_name=f"newsletter_{edition_date}",
        tags={
            "edition_date": edition_date,
            "week_label": week_label,
            "anchor_date": anchor_date,
            "run_type": RUN_TYPE_PIPELINE,
        },
    ) as run:
        _active_run_id = run.info.run_id
        mlflow.log_param("edition_date", edition_date)
        mlflow.log_param("week_label", week_label)
        mlflow.log_param("anchor_date", anchor_date)
        try:
            yield run
        finally:
            flush_monitoring_to_mlflow()
            _active_run_id = None


@contextmanager
def track_stage(stage_name: str):
    """Time a pipeline stage and record it on the active monitor."""
    start = time.perf_counter()
    extra: dict[str, Any] = {}
    try:
        yield extra
    finally:
        duration = time.perf_counter() - start
        if _active_monitor is not None:
            _active_monitor.stages.append(
                StageMetric(name=stage_name, duration_sec=duration, extra=extra)
            )


def record_llm_usage(
    *,
    prompt_tokens: int = 0,
    completion_tokens: int = 0,
    latency_sec: float = 0.0,
    cache_hit: bool = False,
    error: bool = False,
):
    """Accumulate LLM call stats on the active monitoring snapshot."""
    if _active_monitor is None:
        return

    stats = _active_monitor.llm
    if cache_hit:
        stats.cache_hits += 1
        return

    if error:
        stats.errors += 1
        return

    stats.calls += 1
    stats.prompt_tokens += prompt_tokens
    stats.completion_tokens += completion_tokens
    stats.total_tokens += prompt_tokens + completion_tokens
    stats.total_latency_sec += latency_sec


def set_pipeline_counts(*, processed: int, in_newsletter: int):
    if _active_monitor is not None:
        _active_monitor.items_processed = processed
        _active_monitor.items_in_newsletter = in_newsletter


def flush_monitoring_to_mlflow():
    """Write monitoring snapshot metrics to the active MLflow run."""
    import mlflow

    global _active_monitor

    if _active_monitor is None:
        return

    snap = _active_monitor
    total_stage_sec = sum(s.duration_sec for s in snap.stages)

    if total_stage_sec > 0 and snap.items_in_newsletter > 0:
        snap.throughput_items_per_min = (
            snap.items_in_newsletter / total_stage_sec
        ) * 60.0

    for stage in snap.stages:
        name = _sanitize_metric_name(stage.name)
        duration = round(stage.duration_sec, 4)
        mlflow.log_metric(f"stage_{name}_sec", duration)
        mlflow.log_metric(f"stage_{name}_ms", round(duration * 1000, 1))

    mlflow.log_metric("pipeline_total_sec", total_stage_sec)
    mlflow.log_metric("llm_calls", snap.llm.calls)
    mlflow.log_metric("llm_prompt_tokens", snap.llm.prompt_tokens)
    mlflow.log_metric("llm_completion_tokens", snap.llm.completion_tokens)
    mlflow.log_metric("llm_total_tokens", snap.llm.total_tokens)
    mlflow.log_metric("llm_avg_latency_sec", snap.llm.avg_latency_sec)
    mlflow.log_metric("llm_cache_hits", snap.llm.cache_hits)
    mlflow.log_metric("llm_errors", snap.llm.errors)
    mlflow.log_metric("items_processed", snap.items_processed)
    mlflow.log_metric("items_in_newsletter", snap.items_in_newsletter)
    mlflow.log_metric("throughput_items_per_min", snap.throughput_items_per_min)

    if _active_run_id:
        snap.run_id = _active_run_id

    save_monitoring_snapshot(snap)


def save_monitoring_snapshot(snapshot: MonitoringSnapshot) -> Path:
    MONITORING_DIR.mkdir(parents=True, exist_ok=True)
    path = MONITORING_DIR / f"monitoring_{snapshot.edition_date or 'latest'}.json"
    path.write_text(
        json.dumps(snapshot.to_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def load_monitoring_snapshot(edition_date: str) -> MonitoringSnapshot | None:
    path = MONITORING_DIR / f"monitoring_{edition_date}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        llm_data = data.get("llm", {})
        return MonitoringSnapshot(
            edition_date=data.get("edition_date", ""),
            week_label=data.get("week_label", ""),
            run_id=data.get("run_id", ""),
            stages=[StageMetric(**s) for s in data.get("stages", [])],
            llm=LLMUsageStats(**llm_data) if llm_data else LLMUsageStats(),
            items_processed=int(data.get("items_processed", 0)),
            items_in_newsletter=int(data.get("items_in_newsletter", 0)),
            throughput_items_per_min=float(data.get("throughput_items_per_min", 0)),
            recorded_at=data.get("recorded_at", ""),
        )
    except (json.JSONDecodeError, OSError, TypeError):
        return None


def get_active_run_id() -> str | None:
    return _active_run_id


def get_active_monitor() -> MonitoringSnapshot | None:
    return _active_monitor
