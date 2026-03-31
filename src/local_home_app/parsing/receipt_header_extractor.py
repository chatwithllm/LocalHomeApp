"""Receipt header extraction for LocalHomeApp.

Purpose:
- Extract receipt-level fields such as merchant, totals, and payment summary from OCR text.

Inputs:
- OCR text
- provenance identifiers

Outputs:
- partial structured receipt parse record

Dependencies:
- re
- uuid
- merchant_format_detector
- receipt_parse_models

Execution context:
- used before line-item extraction.

Required permissions:
- none directly.

Expected errors/failure modes:
- missing or malformed totals/date fields.

Related tests:
- tests/unit/test_receipt_header_extractor.py

Related docs:
- docs/modules/receipt-header-extractor.md
- docs/phases/phase-03-receipt-parsing.md
"""

from __future__ import annotations

import re
from uuid import uuid4

from local_home_app.parsing.merchant_format_detector import detect_merchant_name
from local_home_app.parsing.receipt_parse_models import ReceiptParseRecord


TOTAL_PATTERN = re.compile(r"\b(?:VISA|TOTAL)\s+(\d+[\s]*[\.,][\s]*\d{2})\b", re.IGNORECASE)
PAYMENT_TOTAL_PATTERN = re.compile(r"\b(?:MASTERCARD|AMEX|DISCOVER|DEBIT|CREDIT)[^\d]*(\d+[\s]*[\.,][\s]*\d{2})\b", re.IGNORECASE)
SUBTOTAL_PATTERN = re.compile(r"\bSUBTOTAL[: ]+(\d+[\s]*[\.,][\s]*\d{2})\b", re.IGNORECASE)
TAX_PATTERN = re.compile(r"\bTAX[^\d]*(\d+[\s]*[\.,][\s]*\d{2})\b", re.IGNORECASE)
DATE_PATTERN = re.compile(r"\b(\d{2}/\d{2}/\d{2})\b")
ALT_DATE_PATTERN = re.compile(r"\b(\d{2}-\d{2}-\d{2})\b")
ALT_LONG_DATE_PATTERN = re.compile(r"\b(\d{2}/\d{2}/\d{4})\b")
TIME_PATTERN = re.compile(r"\b(\d{1,2}:\d{2}(?:am|pm)?)\b", re.IGNORECASE)
COSTCO_TOTAL_BLOCK_PATTERN = re.compile(r"SUBTOTAL\s+([\d\., ]+)\s+TAX\s+([\d\., ]+)\s+TOTAL\s+([\d\., ]+)", re.IGNORECASE | re.DOTALL)


def _normalize_amount(raw_amount: str) -> float:
    cleaned = raw_amount.replace(' ', '').replace(',', '.')
    return float(cleaned)


def extract_receipt_header(*, intake_id: str, ocr_run_id: str, ocr_text: str) -> ReceiptParseRecord:
    merchant_name = detect_merchant_name(ocr_text)

    total_match = TOTAL_PATTERN.search(ocr_text)
    payment_total_match = PAYMENT_TOTAL_PATTERN.search(ocr_text)
    subtotal_match = SUBTOTAL_PATTERN.search(ocr_text)
    tax_match = TAX_PATTERN.search(ocr_text)
    date_match = DATE_PATTERN.search(ocr_text)
    alt_date_match = ALT_DATE_PATTERN.search(ocr_text)
    alt_long_date_match = ALT_LONG_DATE_PATTERN.search(ocr_text)
    time_match = TIME_PATTERN.search(ocr_text)
    costco_total_block_match = COSTCO_TOTAL_BLOCK_PATTERN.search(ocr_text) if merchant_name == 'Costco' else None

    total_value = total_match.group(1) if total_match else None
    if total_value is None and payment_total_match:
        total_value = payment_total_match.group(1)
    if total_value is None and costco_total_block_match:
        total_value = costco_total_block_match.group(3)

    total = _normalize_amount(total_value) if total_value else None
    subtotal = _normalize_amount(subtotal_match.group(1)) if subtotal_match else None
    tax = _normalize_amount(tax_match.group(1)) if tax_match else None
    if subtotal is None and costco_total_block_match:
        subtotal = _normalize_amount(costco_total_block_match.group(1))
    if tax is None and costco_total_block_match:
        tax = _normalize_amount(costco_total_block_match.group(2))
    receipt_date = (
        date_match.group(1)
        if date_match
        else (alt_date_match.group(1) if alt_date_match else (alt_long_date_match.group(1) if alt_long_date_match else None))
    )
    receipt_time = time_match.group(1) if time_match else None

    return ReceiptParseRecord(
        parse_id=str(uuid4()),
        intake_id=intake_id,
        ocr_run_id=ocr_run_id,
        merchant_name=merchant_name,
        receipt_date=receipt_date,
        receipt_time=receipt_time,
        subtotal=subtotal,
        tax=tax,
        total=total,
        payment_method_summary="VISA" if "visa" in ocr_text.lower() else None,
        currency="USD",
        parse_status="partial",
        confidence_summary=None,
        notes=None,
        line_items=[],
    )
