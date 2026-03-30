# Module: apple_vision_bridge.py

## Purpose
Define the macOS-native bridge boundary for Apple-oriented OCR execution.

## Inputs
Local source artifact path.

## Outputs
OCR text or bridge failure information.

## Dependencies
- subprocess
- pathlib

## Execution Context
Used on macOS/Apple hardware when the Apple OCR path is implemented.

## Required Permissions
Local file access and macOS-native bridge/runtime access.

## Expected Errors / Failure Modes
- bridge tooling unavailable
- bridge execution failure

## Related Tests
- tests/unit/test_apple_vision_bridge.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
