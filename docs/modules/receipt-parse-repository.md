# Module: receipt_parse_repository.py

## Purpose
Persist and retrieve structured receipt parse records and line items in SQLite.

## Inputs
Structured receipt parse records.

## Outputs
Stored and loaded parse records.

## Dependencies
- sqlite3
- receipt_parse_models

## Execution Context
Used after receipt parsing.

## Required Permissions
Read/write access to local database.

## Expected Errors / Failure Modes
- insert or query failures

## Related Tests
- tests/unit/test_receipt_parse_repository.py

## Related Docs
- docs/phases/phase-04-local-storage.md
