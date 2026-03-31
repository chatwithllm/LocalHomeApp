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
import json
import subprocess
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class AppleVisionBridgeResult:
    success: bool
    ocr_text: str
    error_message: Optional[str] = None


def _project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _bridge_source_path() -> Path:
    return _project_root() / "scripts" / "apple_vision_bridge" / "apple_vision_ocr.swift"


def _bridge_binary_path() -> Path:
    return _project_root() / ".tmp" / "apple_vision_ocr_bridge"


def _compile_bridge_if_needed() -> AppleVisionBridgeResult | None:
    source_path = _bridge_source_path()
    binary_path = _bridge_binary_path()

    if not source_path.exists():
        return AppleVisionBridgeResult(
            success=False,
            ocr_text="",
            error_message=f"Apple Vision bridge source is missing: {source_path}",
        )

    binary_path.parent.mkdir(parents=True, exist_ok=True)

    if binary_path.exists() and binary_path.stat().st_mtime >= source_path.stat().st_mtime:
        return None

    compile_command = [
        "xcrun",
        "swiftc",
        "-framework",
        "Vision",
        "-framework",
        "AppKit",
        str(source_path),
        "-o",
        str(binary_path),
    ]

    try:
        completed = subprocess.run(
            compile_command,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return AppleVisionBridgeResult(
            success=False,
            ocr_text="",
            error_message="xcrun/swiftc not available for Apple Vision bridge compilation",
        )

    if completed.returncode != 0:
        stderr = (completed.stderr or completed.stdout or "").strip()
        return AppleVisionBridgeResult(
            success=False,
            ocr_text="",
            error_message=f"Apple Vision bridge compilation failed: {stderr}",
        )

    return None


def run_apple_vision_bridge(source_artifact_path: Path) -> AppleVisionBridgeResult:
    """Run the Apple OCR bridge through a macOS-native Swift/Vision helper."""

    compile_result = _compile_bridge_if_needed()
    if compile_result is not None:
        return compile_result

    binary_path = _bridge_binary_path()
    command = [str(binary_path), str(source_artifact_path)]

    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return AppleVisionBridgeResult(
            success=False,
            ocr_text="",
            error_message="compiled Apple Vision bridge binary is unavailable",
        )

    payload_text = (completed.stdout or "").strip()
    if not payload_text:
        stderr = (completed.stderr or "").strip()
        return AppleVisionBridgeResult(
            success=False,
            ocr_text="",
            error_message=f"Apple Vision bridge returned no JSON output: {stderr}",
        )

    try:
        payload = json.loads(payload_text)
    except json.JSONDecodeError:
        stderr = (completed.stderr or "").strip()
        return AppleVisionBridgeResult(
            success=False,
            ocr_text="",
            error_message=f"Apple Vision bridge returned invalid JSON: {stderr or payload_text}",
        )

    return AppleVisionBridgeResult(
        success=bool(payload.get("success")),
        ocr_text=str(payload.get("ocr_text") or ""),
        error_message=payload.get("error_message"),
    )
