# Module: ocr_comparison_models.py

## Purpose
Represent structured comparison results between multiple OCR runs.

## Inputs
OCR result records from different engine or preprocessing variants.

## Outputs
Structured OCR comparison records.

## Dependencies
- dataclasses
- typing
- ocr_result_models

## Execution Context
Used by OCR comparison workflows.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- missing comparison labels or OCR references

## Related Tests
- tests/unit/test_ocr_comparison_models.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
