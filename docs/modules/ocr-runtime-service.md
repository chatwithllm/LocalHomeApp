# Module: ocr_runtime_service.py

## Purpose
Provide a simple orchestration entry point for OCR engine execution.

## Inputs
OCR engine implementation, intake ID, source artifact path.

## Outputs
OCR result record.

## Dependencies
- pathlib
- ocr_engine_interface
- ocr_result_models

## Execution Context
Used by later OCR workflow layers.

## Required Permissions
Depends on selected OCR engine implementation.

## Expected Errors / Failure Modes
- engine execution failure

## Related Tests
- tests/unit/test_ocr_runtime_service.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
