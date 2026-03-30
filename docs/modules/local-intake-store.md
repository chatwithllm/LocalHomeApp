# Module: local_intake_store.py

## Purpose
Provide a temporary Phase 1 file-backed intake metadata store using JSONL.

## Inputs
Intake event records.

## Outputs
Persisted and reloadable intake metadata records.

## Dependencies
- json
- dataclasses
- pathlib

## Execution Context
Used before the database-backed store is implemented.

## Required Permissions
Read/write access to local sensitive storage root.

## Expected Errors / Failure Modes
- unwritable metadata file
- invalid JSONL content

## Related Tests
- tests/unit/test_local_intake_store.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
