# Module: ocr_result_models.py

## Purpose
Represent OCR outputs and execution metadata with clear provenance.

## Inputs
OCR engine outputs and execution metadata.

## Outputs
Structured OCR result records.

## Dependencies
- dataclasses
- typing

## Execution Context
Used by OCR runtime and storage components.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- missing required provenance fields

## Related Tests
- tests/unit/test_ocr_result_models.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
