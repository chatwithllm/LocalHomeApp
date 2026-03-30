# Module: receipt_parse_runtime_service.py

## Purpose
Orchestrate receipt parsing from OCR text into structured and validated parse records.

## Inputs
Intake identifier, OCR run identifier, and OCR text.

## Outputs
Validated structured receipt parse record.

## Dependencies
- receipt_header_extractor
- receipt_line_item_extractor
- receipt_parse_validator
- dataclasses.replace

## Execution Context
Used by future OCR-to-parsing handoff workflows.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- OCR text too noisy for useful parsing

## Related Tests
- tests/unit/test_receipt_parse_runtime_service.py

## Related Docs
- docs/phases/phase-03-receipt-parsing.md
