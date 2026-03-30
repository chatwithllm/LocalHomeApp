"""Receipt line-item extraction boundary for LocalHomeApp.

Purpose:
- Provide the current boundary for extracting item-level lines from OCR text.

Inputs:
- OCR text
- parse identifier

Outputs:
- line-item record list

Dependencies:
- receipt_parse_models

Execution context:
- used after header extraction.

Required permissions:
- none directly.

Expected errors/failure modes:
- noisy OCR line segmentation.

Related tests:
- tests/unit/test_receipt_line_item_extractor.py

Related docs:
- docs/modules/receipt-line-item-extractor.md
- docs/phases/phase-03-receipt-parsing.md
"""

from __future__ import annotations

from typing import List
from uuid import uuid4

from local_home_app.parsing.receipt_parse_models import ReceiptLineItemRecord


import re

ITEM_EXCLUSION_HINTS = [
    "visa",
    "mastercard",
    "total",
    "subtotal",
    "tax",
    "savings",
    "fuel points",
    "change",
    "feedback",
    "jobs",
    "annual card",
    "balance",
    "receipt details",
    "save money. live better.",
    "walmart >",
    "wal*mart",
    "kroger",
    "meijer",
    "cash back",
    "items sold",
    "sales receipt",
    "customer:",
    "csr:",
    "general manager",
    "auth code",
    "reference;",
    "number of items purchased",
    "payment tender",
    "approval code",
]
STRUCTURE_EXCLUSION_HINTS = ["st#", "op#", "te#", "tr#", "tc#", "mgr.", "sales id:", "s/n:", "txt", "tm:"]
PRICE_PATTERN = re.compile(r"(\d+[\s]*[\.,][\s]*\d{2})")
ALPHA_PATTERN = re.compile(r"[A-Za-z]{3,}")
AMOUNT_ONLY_PATTERN = re.compile(r"^\d+[\s]*[\.,][\s]*\d{2}$")
CITY_STATE_PATTERN = re.compile(r"^[A-Za-z .'-]+,\s*[A-Z]{2}(?:\s+\d{5})?$")


def extract_line_items(*, parse_id: str, ocr_text: str) -> List[ReceiptLineItemRecord]:
    items: List[ReceiptLineItemRecord] = []
    for line in [segment.strip() for segment in ocr_text.splitlines() if segment.strip()]:
        normalized = line.lower()
        if any(hint in normalized for hint in ITEM_EXCLUSION_HINTS):
            continue
        if any(hint in normalized for hint in STRUCTURE_EXCLUSION_HINTS):
            continue
        if len(line) < 4:
            continue
        if AMOUNT_ONLY_PATTERN.match(line):
            continue
        if CITY_STATE_PATTERN.match(line):
            continue
        if normalized.startswith('date:') or normalized.startswith('| date:'):
            continue
        if normalized.startswith('sales ') or normalized.startswith('sales[') or normalized.startswith('sales id'):
            continue
        if not ALPHA_PATTERN.search(line):
            continue

        price_match = PRICE_PATTERN.search(line)
        item_name = line
        line_total = None
        confidence_summary = "low"
        if price_match:
            line_total = float(price_match.group(1).replace(' ', '').replace(',', '.'))
            item_name = line[: price_match.start()].strip() or line
            confidence_summary = "medium"

        if len(item_name.strip()) < 3:
            continue

        items.append(
            ReceiptLineItemRecord(
                line_id=str(uuid4()),
                parse_id=parse_id,
                raw_text=line,
                item_name=item_name,
                quantity=None,
                unit_price=None,
                line_total=line_total,
                discount_text=None,
                confidence_summary=confidence_summary,
            )
        )
    return items
