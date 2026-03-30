# Module: ocr_comparison_runner.py

## Purpose
Run multiple OCR variants against a single artifact and package the results for comparison.

## Inputs
Intake identifier, source artifact path, and OCR engine variants with labels.

## Outputs
Structured OCR comparison record.

## Dependencies
- uuid
- pathlib
- ocr_comparison_models
- ocr_engine_interface

## Execution Context
Used by OCR comparison workflows.

## Required Permissions
Depends on selected OCR engine implementations.

## Expected Errors / Failure Modes
- OCR engine execution failures
- invalid comparison configuration

## Related Tests
- tests/unit/test_ocr_comparison_runner.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
