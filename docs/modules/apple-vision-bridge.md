# Module: apple_vision_bridge.py

## Purpose
Define and execute the macOS-native Swift/Vision bridge for Apple-oriented OCR execution.

## Inputs
Local source artifact path.

## Outputs
OCR text or bridge failure information.

## Dependencies
- subprocess
- pathlib

## Execution Context
Used on macOS/Apple hardware. The Python layer compiles a local Swift helper against Vision/AppKit with `xcrun swiftc` and executes it against a local image path.

## Required Permissions
Local file access and macOS-native bridge/runtime access.

## Expected Errors / Failure Modes
- bridge source missing
- Xcode/Command Line Tools or `xcrun swiftc` unavailable
- Swift bridge compilation failure
- Vision OCR execution failure
- unsupported/unreadable image input

## Related Tests
- tests/unit/test_apple_vision_bridge.py

## Related Docs
- docs/phases/phase-02-dual-local-ocr.md
