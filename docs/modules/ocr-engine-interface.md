# Module: ocr_engine_interface.py

## Purpose
Define the common OCR engine interface for LocalHomeApp.

## Inputs
Local source artifact path and intake provenance identifiers.

## Outputs
Structured OCR result records.

## Dependencies
- abc
- pathlib
- ocr_result_models

## Execution Context
Implemented by engine-specific OCR modules.

## Required Permissions
Depends on engine implementation.

## Expected Errors / Failure Modes
- engine-specific runtime failures

## Related Tests
- tests/unit/test_ocr_engine_interface.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
