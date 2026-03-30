# Module: receipt_parse_store.py

## Purpose
Persist structured receipt parse results locally in a simple file-backed format during early Phase 3.

## Inputs
Structured receipt parse records.

## Outputs
Persisted and reloadable parse records.

## Dependencies
- json
- dataclasses
- pathlib

## Execution Context
Used by parsing runtime workflows before database-backed parse storage is introduced.

## Required Permissions
Read/write access to local sensitive parse storage.

## Expected Errors / Failure Modes
- invalid JSONL content
- unwritable local storage path

## Related Tests
- tests/unit/test_receipt_parse_store.py

## Related Docs
- docs/phases/phase-03-receipt-parsing.md
