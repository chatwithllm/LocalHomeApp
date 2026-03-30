# Module: receipt_deduplication.py

## Purpose
Provide duplicate-detection helpers for receipt intake.

## Inputs
Telegram file identity values, content hashes, and existing intake event records.

## Outputs
Duplicate match decisions.

## Dependencies
- intake_event_store

## Execution Context
Used during receipt intake before downstream processing.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- ambiguous or incomplete metadata for comparison

## Related Tests
- tests/unit/test_receipt_deduplication.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
