"""OCR evaluation summary helpers for LocalHomeApp.

Purpose:
- Turn raw OCR comparison results into a practical summary that can be inspected in tests, scripts, and docs.

Inputs:
- OCR comparison record

Outputs:
- structured evaluation summary and text rendering

Dependencies:
- dataclasses
- typing
- ocr_comparison_models

Execution context:
- used by real-receipt OCR evaluation flows.

Required permissions:
- none directly.

Expected errors/failure modes:
- empty comparison records provide sparse summaries

Related tests:
- tests/unit/test_ocr_evaluation_summary.py

Related docs:
- docs/modules/ocr-evaluation-summary.md
- docs/phases/phase-09-real-receipt-evaluation.md
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from local_home_app.ocr.ocr_comparison_models import OcrComparisonRecord


@dataclass(frozen=True)
class OcrEvaluationEntrySummary:
    label: str
    status: str
    runtime_ms: int | None
    text_length: int
    line_count: int
    preview: str


@dataclass(frozen=True)
class OcrEvaluationSummary:
    comparison_id: str
    intake_id: str
    completed_labels: List[str] = field(default_factory=list)
    failed_labels: List[str] = field(default_factory=list)
    entries: List[OcrEvaluationEntrySummary] = field(default_factory=list)


def summarize_ocr_comparison(record: OcrComparisonRecord) -> OcrEvaluationSummary:
    entries: List[OcrEvaluationEntrySummary] = []
    completed_labels: List[str] = []
    failed_labels: List[str] = []

    for entry in record.entries:
        text = entry.result.ocr_text or ""
        preview = "\n".join(line.strip() for line in text.splitlines()[:3]).strip()
        summary = OcrEvaluationEntrySummary(
            label=entry.label,
            status=entry.result.status,
            runtime_ms=entry.result.runtime_ms,
            text_length=len(text.strip()),
            line_count=len([line for line in text.splitlines() if line.strip()]),
            preview=preview,
        )
        entries.append(summary)
        if entry.result.status == "completed":
            completed_labels.append(entry.label)
        else:
            failed_labels.append(entry.label)

    return OcrEvaluationSummary(
        comparison_id=record.comparison_id,
        intake_id=record.intake_id,
        completed_labels=completed_labels,
        failed_labels=failed_labels,
        entries=entries,
    )


def render_ocr_evaluation_summary(summary: OcrEvaluationSummary) -> str:
    lines = [
        f"OCR comparison: {summary.intake_id}",
        f"Completed: {', '.join(summary.completed_labels) if summary.completed_labels else 'none'}",
        f"Non-completed: {', '.join(summary.failed_labels) if summary.failed_labels else 'none'}",
    ]
    for entry in summary.entries:
        lines.append(
            f"- {entry.label}: status={entry.status}, runtime_ms={entry.runtime_ms}, "
            f"lines={entry.line_count}, text_length={entry.text_length}"
        )
        if entry.preview:
            lines.append(f"  preview: {entry.preview}")
    return "\n".join(lines)
