"""Merchant and format detection for LocalHomeApp receipt parsing.

Purpose:
- Detect likely merchant or receipt format family from OCR text.

Inputs:
- OCR text

Outputs:
- detected merchant/format hint

Dependencies:
- none beyond standard library

Execution context:
- used before detailed parsing rules are applied.

Required permissions:
- none directly.

Expected errors/failure modes:
- low-confidence or unknown merchant detection.

Related tests:
- tests/unit/test_merchant_format_detector.py

Related docs:
- docs/modules/merchant-format-detector.md
- docs/phases/phase-03-receipt-parsing.md
"""

from __future__ import annotations


def detect_merchant_name(ocr_text: str) -> str | None:
    normalized = ocr_text.lower()
    if "costco" in normalized:
        return "Costco"
    if "kroger" in normalized:
        return "Kroger"
    if "walmart" in normalized or "wal*mart" in normalized:
        return "Walmart"
    if "micro center" in normalized or "icro center" in normalized:
        return "Micro Center"
    if "meijer" in normalized or "metljer" in normalized:
        return "Meijer"
    return None
