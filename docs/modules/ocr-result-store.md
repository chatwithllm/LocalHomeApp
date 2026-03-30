# Module: ocr_result_store.py

## Purpose
Persist OCR results locally in a simple file-backed format during early Phase 2.

## Inputs
OCR result records.

## Outputs
Persisted and reloadable OCR result records.

## Dependencies
- json
- dataclasses
- pathlib

## Execution Context
Used by OCR runtime workflows before a database-backed OCR store is introduced.

## Required Permissions
Read/write access to local sensitive OCR storage.

## Expected Errors / Failure Modes
- invalid JSONL content
- unwritable local storage path

## Related Tests
- tests/unit/test_ocr_result_store.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
