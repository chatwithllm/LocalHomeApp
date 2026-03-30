# Module: receipt_parse_validator.py

## Purpose
Validate parse completeness and assign a high-level parse status.

## Inputs
Structured receipt parse record.

## Outputs
Updated parse record with validation-aware status.

## Dependencies
- dataclasses.replace
- receipt_parse_models

## Execution Context
Used after header and line-item extraction.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- missing required core fields

## Related Tests
- tests/unit/test_receipt_parse_validator.py

## Related Docs
- docs/phases/phase-03-receipt-parsing.md
