# Module: intake_workflow.py

## Purpose
Construct intake event metadata records from normalized Telegram candidates and stored local files.

## Inputs
Telegram receipt candidate, stored local path, content hash.

## Outputs
Structured intake event metadata records.

## Dependencies
- uuid
- intake_event_store
- telegram_receipt_ingest

## Execution Context
Used after receipt download planning/execution.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- missing provenance values
- invalid storage path values

## Related Tests
- tests/unit/test_intake_workflow.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
