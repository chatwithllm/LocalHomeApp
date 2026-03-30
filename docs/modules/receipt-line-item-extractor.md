# Module: receipt_line_item_extractor.py

## Purpose
Provide the current boundary for extracting item-level lines from OCR text.

## Inputs
OCR text and parse identifier.

## Outputs
Line-item record list.

## Dependencies
- receipt_parse_models

## Execution Context
Used after header extraction.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- noisy OCR line segmentation

## Related Tests
- tests/unit/test_receipt_line_item_extractor.py

## Related Docs
- docs/phases/phase-03-receipt-parsing.md
