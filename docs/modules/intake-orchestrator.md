# Module: intake_orchestrator.py

## Purpose
Run the Phase 1 local intake orchestration workflow across path planning, file writing, hashing, duplicate detection, and metadata persistence.

## Inputs
Telegram receipt candidate, file bytes, filesystem path helper, and local intake store.

## Outputs
Intake orchestration result containing the stored record and duplicate information.

## Dependencies
- telegram_media_download
- file_hashing
- intake_workflow
- receipt_deduplication
- local_intake_store

## Execution Context
Used by the local intake service after receipt candidate normalization.

## Required Permissions
Read/write access to local sensitive storage root.

## Expected Errors / Failure Modes
- file write failure
- hashing failure
- metadata persistence failure

## Related Tests
- tests/unit/test_intake_orchestrator.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
