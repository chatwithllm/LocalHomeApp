# Module: ocr_result_repository.py

## Purpose
Persist and retrieve OCR result records in SQLite.

## Inputs
OCR result records.

## Outputs
Stored and loaded OCR result records.

## Dependencies
- sqlite3
- ocr_result_models

## Execution Context
Used after OCR execution.

## Required Permissions
Read/write access to local database.

## Expected Errors / Failure Modes
- insert or query failures

## Related Tests
- tests/unit/test_ocr_result_repository.py

## Related Docs
- docs/phases/phase-04-local-storage.md
