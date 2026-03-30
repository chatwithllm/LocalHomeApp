"""Receipt parse models for LocalHomeApp.

Purpose:
- Represent structured receipt parse outputs with receipt-level and line-item-level data.

Inputs:
- OCR text interpretation results.

Outputs:
- structured parse result records.

Dependencies:
- dataclasses
- typing

Execution context:
- used by parsing runtime and validation components.

Required permissions:
- none directly.

Expected errors/failure modes:
- missing required provenance fields.

Related tests:
- tests/unit/test_receipt_parse_models.py

Related docs:
- docs/modules/receipt-parse-models.md
- docs/phases/phase-03-receipt-parsing.md
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class ReceiptLineItemRecord:
    line_id: str
    parse_id: str
    raw_text: str
    item_name: Optional[str]
    quantity: Optional[float]
    unit_price: Optional[float]
    line_total: Optional[float]
    discount_text: Optional[str]
    confidence_summary: Optional[str]


@dataclass(frozen=True)
class ReceiptParseRecord:
    parse_id: str
    intake_id: str
    ocr_run_id: str
    merchant_name: Optional[str]
    receipt_date: Optional[str]
    receipt_time: Optional[str]
    subtotal: Optional[float]
    tax: Optional[float]
    total: Optional[float]
    payment_method_summary: Optional[str]
    currency: Optional[str]
    parse_status: str
    confidence_summary: Optional[str]
    notes: Optional[str]
    line_items: List[ReceiptLineItemRecord] = field(default_factory=list)
