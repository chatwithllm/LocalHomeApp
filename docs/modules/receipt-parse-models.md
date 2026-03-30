# Module: receipt_parse_models.py

## Purpose
Represent structured receipt parse outputs with receipt-level and line-item-level data.

## Inputs
OCR text interpretation results.

## Outputs
Structured parse result records.

## Dependencies
- dataclasses
- typing

## Execution Context
Used by parsing runtime and validation components.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- missing required provenance fields

## Related Tests
- tests/unit/test_receipt_parse_models.py

## Related Docs
- docs/phases/phase-03-receipt-parsing.md
