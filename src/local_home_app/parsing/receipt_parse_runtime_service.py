"""Receipt parse runtime service for LocalHomeApp.

Purpose:
- Orchestrate receipt parsing from OCR text into structured and validated parse records.

Inputs:
- intake identifier
- OCR run identifier
- OCR text

Outputs:
- validated structured receipt parse record

Dependencies:
- receipt_header_extractor
- receipt_line_item_extractor
- receipt_parse_validator
- dataclasses.replace

Execution context:
- used by future OCR-to-parsing handoff workflows.

Required permissions:
- none directly.

Expected errors/failure modes:
- OCR text too noisy for useful parsing.

Related tests:
- tests/unit/test_receipt_parse_runtime_service.py

Related docs:
- docs/modules/receipt-parse-runtime-service.md
- docs/phases/phase-03-receipt-parsing.md
"""

from __future__ import annotations

from dataclasses import replace

from local_home_app.parsing.receipt_header_extractor import extract_receipt_header
from local_home_app.parsing.receipt_line_item_extractor import extract_line_items
from local_home_app.parsing.receipt_parse_models import ReceiptParseRecord
from local_home_app.parsing.receipt_parse_validator import validate_receipt_parse


def run_receipt_parse(*, intake_id: str, ocr_run_id: str, ocr_text: str) -> ReceiptParseRecord:
    header = extract_receipt_header(intake_id=intake_id, ocr_run_id=ocr_run_id, ocr_text=ocr_text)
    line_items = extract_line_items(parse_id=header.parse_id, ocr_text=ocr_text)
    combined = replace(header, line_items=line_items)
    return validate_receipt_parse(combined)
