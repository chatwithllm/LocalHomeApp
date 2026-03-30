# Module: tesseract_ocr.py

## Purpose
Provide the portable OCR engine implementation path for Tesseract-based OCR, including optional preprocessing.

## Inputs
Intake identifier and local source artifact path.

## Outputs
Structured OCR result record.

## Dependencies
- pathlib
- shutil
- subprocess
- time
- uuid
- receipt_image_preprocessor
- ocr_engine_interface
- ocr_result_models

## Execution Context
Used on portable/local environments where Tesseract is installed.

## Required Permissions
Local file access and local process execution.

## Expected Errors / Failure Modes
- Tesseract binary not installed
- OCR command failure
- preprocessing failure

## Related Tests
- tests/unit/test_tesseract_ocr.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
