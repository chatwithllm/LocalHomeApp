# Module: receipt_header_extractor.py

## Purpose
Extract receipt-level fields such as merchant, totals, and payment summary from OCR text.

## Inputs
OCR text and provenance identifiers.

## Outputs
Partial structured receipt parse record.

## Dependencies
- re
- uuid
- merchant_format_detector
- receipt_parse_models

## Execution Context
Used before line-item extraction.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- missing or malformed totals/date fields

## Related Tests
- tests/unit/test_receipt_header_extractor.py

## Related Docs
- docs/phases/phase-03-receipt-parsing.md
