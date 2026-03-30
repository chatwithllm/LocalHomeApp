"""Output runtime orchestration for LocalHomeApp.

Purpose:
- Assemble structured output summaries from receipt, history, and signal data.

Inputs:
- receipt summary
- purchase history summary
- signal summary

Outputs:
- local report text and Telegram summary text

Dependencies:
- local_report_builder
- telegram_summary_formatter
- output_models

Execution context:
- used by future output/integration workflows.

Required permissions:
- none directly.

Expected errors/failure modes:
- incomplete upstream summary data

Related tests:
- tests/unit/test_output_runtime_service.py

Related docs:
- docs/modules/output-runtime-service.md
- docs/phases/phase-06-output-integration.md
"""

from __future__ import annotations

from dataclasses import dataclass

from local_home_app.output.local_report_builder import build_local_report
from local_home_app.output.output_models import (
    PurchaseHistorySummaryOutput,
    ReceiptSummaryOutput,
    SignalSummaryOutput,
)
from local_home_app.output.telegram_summary_formatter import format_telegram_summary


@dataclass(frozen=True)
class OutputRuntimeResult:
    local_report: str
    telegram_summary: str


def build_outputs(
    *,
    receipt_summary: ReceiptSummaryOutput,
    purchase_history_summary: PurchaseHistorySummaryOutput,
    signal_summary: SignalSummaryOutput,
) -> OutputRuntimeResult:
    return OutputRuntimeResult(
        local_report=build_local_report(
            receipt_summary=receipt_summary,
            purchase_history_summary=purchase_history_summary,
            signal_summary=signal_summary,
        ),
        telegram_summary=format_telegram_summary(
            receipt_summary=receipt_summary,
            signal_summary=signal_summary,
        ),
    )
