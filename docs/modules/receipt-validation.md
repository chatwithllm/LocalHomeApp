# Module: receipt_validation.py

## Purpose
Validate whether an intake candidate uses an allowed receipt-like file format.

## Inputs
Telegram receipt candidate.

## Outputs
Validation result indicating acceptance or rejection.

## Dependencies
- dataclasses
- telegram_receipt_ingest

## Execution Context
Used before live intake processing stores local files.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- unsupported mime types
- unsupported file extensions

## Related Tests
- tests/unit/test_receipt_validation.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
