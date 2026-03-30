"""Receipt parse validation for LocalHomeApp.

Purpose:
- Validate parse completeness and assign a high-level parse status.

Inputs:
- structured receipt parse record

Outputs:
- updated parse record with validation-aware status

Dependencies:
- dataclasses.replace
- receipt_parse_models

Execution context:
- used after header and line-item extraction.

Required permissions:
- none directly.

Expected errors/failure modes:
- missing required core fields.

Related tests:
- tests/unit/test_receipt_parse_validator.py

Related docs:
- docs/modules/receipt-parse-validator.md
- docs/phases/phase-03-receipt-parsing.md
"""

from __future__ import annotations

from dataclasses import replace

from local_home_app.parsing.receipt_parse_models import ReceiptParseRecord


def validate_receipt_parse(record: ReceiptParseRecord) -> ReceiptParseRecord:
    notes = []
    if record.merchant_name is None:
        notes.append("merchant_missing")
    if record.total is None:
        notes.append("total_missing")
    if not record.line_items:
        notes.append("line_items_missing")

    if record.merchant_name and record.total is not None:
        return replace(
            record,
            parse_status="completed",
            confidence_summary="medium",
            notes=", ".join(notes) if notes else None,
        )
    if record.total is not None or record.merchant_name:
        return replace(
            record,
            parse_status="partial",
            confidence_summary="low",
            notes=", ".join(notes) if notes else None,
        )
    return replace(
        record,
        parse_status="low_confidence",
        confidence_summary="low",
        notes=", ".join(notes) if notes else None,
    )
