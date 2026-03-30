# Module: receipt_intake_repository.py

## Purpose
Persist and retrieve receipt intake event records in SQLite.

## Inputs
Receipt intake event records.

## Outputs
Stored and loaded intake records.

## Dependencies
- sqlite3
- intake_event_store

## Execution Context
Used by storage workflows after intake processing.

## Required Permissions
Read/write access to local database.

## Expected Errors / Failure Modes
- insert or query failures

## Related Tests
- tests/unit/test_receipt_intake_repository.py

## Related Docs
- docs/phases/phase-04-local-storage.md
