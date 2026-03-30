# Module: ocr_comparison_store.py

## Purpose
Persist OCR comparison results locally in a simple file-backed format.

## Inputs
OCR comparison records.

## Outputs
Persisted and reloadable OCR comparison records.

## Dependencies
- json
- dataclasses
- pathlib

## Execution Context
Used by OCR comparison workflows.

## Required Permissions
Read/write access to local sensitive OCR storage.

## Expected Errors / Failure Modes
- invalid JSONL content
- unwritable local storage path

## Related Tests
- tests/unit/test_ocr_comparison_store.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
