# Module: merchant_format_detector.py

## Purpose
Detect likely merchant or receipt format family from OCR text.

## Inputs
OCR text.

## Outputs
Detected merchant/format hint.

## Dependencies
Standard library only.

## Execution Context
Used before detailed parsing rules are applied.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- low-confidence or unknown merchant detection

## Related Tests
- tests/unit/test_merchant_format_detector.py

## Related Docs
- docs/phases/phase-03-receipt-parsing.md
