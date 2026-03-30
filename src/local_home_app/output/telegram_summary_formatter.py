"""Telegram summary formatting for LocalHomeApp.

Purpose:
- Build concise Telegram-friendly summary text from structured outputs.

Inputs:
- receipt summary
- signal summary

Outputs:
- formatted summary message

Dependencies:
- output_models

Execution context:
- used by future integration/output handoff flows.

Required permissions:
- none directly.

Expected errors/failure modes:
- incomplete summary data

Related tests:
- tests/unit/test_telegram_summary_formatter.py

Related docs:
- docs/modules/telegram-summary-formatter.md
- docs/phases/phase-06-output-integration.md
"""

from __future__ import annotations

from local_home_app.output.output_models import ReceiptSummaryOutput, SignalSummaryOutput


def format_telegram_summary(
    *, receipt_summary: ReceiptSummaryOutput, signal_summary: SignalSummaryOutput
) -> str:
    lines = [
        f"Receipt: {receipt_summary.merchant_name or 'Unknown merchant'}",
        f"Date: {receipt_summary.receipt_date or 'Unknown date'}",
        f"Total: {receipt_summary.total if receipt_summary.total is not None else 'Unknown'}",
        f"Status: {receipt_summary.parse_status}",
    ]
    if signal_summary.lines:
        lines.append("Signals:")
        lines.extend(signal_summary.lines[:5])
    return "\n".join(lines)
