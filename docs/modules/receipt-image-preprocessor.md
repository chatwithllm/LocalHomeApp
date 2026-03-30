# Module: receipt_image_preprocessor.py

## Purpose
Improve receipt images for OCR by generating a grayscale, autocontrasted preprocessed copy when appropriate.

## Inputs
Local source artifact path and optional destination directory.

## Outputs
Preprocessed artifact path or passthrough source path.

## Dependencies
- pathlib
- Pillow

## Execution Context
Used before OCR execution when preprocessing is beneficial.

## Required Permissions
Read/write access to local OCR artifact storage.

## Expected Errors / Failure Modes
- unsupported image format
- preprocessing runtime failure

## Related Tests
- tests/unit/test_receipt_image_preprocessor.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
