"""Local report building for LocalHomeApp.

Purpose:
- Build compact local text reports from summaries and signals.

Inputs:
- receipt summary
- purchase history summary
- signal summary

Outputs:
- local report text

Dependencies:
- output_models

Execution context:
- used for local reporting and export preparation.

Required permissions:
- none directly.

Expected errors/failure modes:
- incomplete output metadata

Related tests:
- tests/unit/test_local_report_builder.py

Related docs:
- docs/modules/local-report-builder.md
- docs/phases/phase-06-output-integration.md
"""

from __future__ import annotations

from local_home_app.output.output_models import (
    PurchaseHistorySummaryOutput,
    ReceiptSummaryOutput,
    SignalSummaryOutput,
)


def build_local_report(
    *,
    receipt_summary: ReceiptSummaryOutput,
    purchase_history_summary: PurchaseHistorySummaryOutput,
    signal_summary: SignalSummaryOutput,
) -> str:
    lines = [
        f"Merchant: {receipt_summary.merchant_name}",
        f"Date: {receipt_summary.receipt_date}",
        f"Total: {receipt_summary.total}",
        f"Parse status: {receipt_summary.parse_status}",
        f"Receipts tracked: {purchase_history_summary.receipt_count}",
    ]
    if purchase_history_summary.merchants:
        lines.append("Merchants: " + ", ".join(purchase_history_summary.merchants))
    if signal_summary.lines:
        lines.append("Signals:")
        lines.extend(signal_summary.lines)
    return "\n".join(lines)
