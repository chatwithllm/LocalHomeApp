# Module: apple_vision_ocr.py

## Purpose
Provide the Apple-oriented OCR engine through a real macOS-native Swift/Vision bridge.

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
Local file access and macOS-native OCR bridge/runtime access through Swift/Vision tooling.

## Expected Errors / Failure Modes
- bridge compilation/runtime failure
- unreadable local image input
- local Apple OCR unavailable on non-macOS or incomplete toolchain setups

## Related Tests
- tests/unit/test_apple_vision_ocr.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
