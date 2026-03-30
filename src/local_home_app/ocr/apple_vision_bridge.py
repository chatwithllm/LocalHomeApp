"""Apple Vision bridge scaffolding for LocalHomeApp.

Purpose:
- Define the macOS-native bridge boundary for Apple-oriented OCR execution.

Inputs:
- local source artifact path

Outputs:
- OCR text or bridge failure information

Dependencies:
- subprocess
- pathlib

Execution context:
- used on macOS/Apple hardware when the Apple OCR path is implemented.

Required permissions:
- local file access
- macOS-native bridge/runtime access

Expected errors/failure modes:
- bridge tooling unavailable
- bridge execution failure

Related tests:
- tests/unit/test_apple_vision_bridge.py

Related docs:
- docs/modules/apple-vision-bridge.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class AppleVisionBridgeResult:
    success: bool
    ocr_text: str
    error_message: Optional[str] = None


def run_apple_vision_bridge(source_artifact_path: Path) -> AppleVisionBridgeResult:
    """Run the Apple OCR bridge.

    Current Phase 2 behavior: scaffold only until the chosen macOS-native bridge is implemented.
    """

    return AppleVisionBridgeResult(
        success=False,
        ocr_text="",
        error_message="Apple Vision bridge not yet implemented in this environment",
    )
