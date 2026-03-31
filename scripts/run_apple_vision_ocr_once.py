#!/usr/bin/env python3
"""Run the Apple Vision OCR bridge once for a local artifact.

Purpose:
- Provide a simple local validation path for the macOS-native Apple Vision OCR bridge.

Inputs:
- intake identifier
- local source artifact path

Outputs:
- JSON summary of the OCR result

Dependencies:
- argparse
- json
- pathlib
- apple_vision_ocr

Execution context:
- run manually on macOS environments with Swift/Vision available.

Required permissions:
- local file access
- local Xcode/Command Line Tools runtime access

Expected errors/failure modes:
- bridge compilation failure
- unsupported file type
- OCR runtime failure

Related docs:
- docs/modules/apple-vision-bridge.md
- docs/modules/apple-vision-ocr.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.ocr.apple_vision_ocr import AppleVisionOcrEngine


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Apple Vision OCR once for a local artifact")
    parser.add_argument("source_artifact_path", help="Path to a local image artifact")
    parser.add_argument("--intake-id", default="apple-vision-demo", help="Logical intake identifier")
    args = parser.parse_args()

    engine = AppleVisionOcrEngine()
    result = engine.run_ocr(intake_id=args.intake_id, source_artifact_path=Path(args.source_artifact_path))
    print(
        json.dumps(
            {
                "ocr_run_id": result.ocr_run_id,
                "engine_name": result.engine_name,
                "status": result.status,
                "runtime_ms": result.runtime_ms,
                "error_message": result.error_message,
                "ocr_text_preview": result.ocr_text[:500],
            },
            indent=2,
        )
    )
    return 0 if result.status == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
