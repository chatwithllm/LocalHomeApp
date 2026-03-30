# Module: apple_vision_ocr.py

## Purpose
Provide the Apple-oriented OCR engine boundary through a macOS-native bridge.

## Inputs
Intake identifier and local source artifact path.

## Outputs
Structured OCR result record.

## Dependencies
- pathlib
- time
- uuid
- apple_vision_bridge
- ocr_engine_interface
- ocr_result_models

## Execution Context
Used on Apple hardware environments.

## Required Permissions
Local file access and macOS-native OCR bridge/runtime access when implemented.

## Expected Errors / Failure Modes
- bridge not yet implemented
- bridge execution failure

## Related Tests
- tests/unit/test_apple_vision_ocr.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
