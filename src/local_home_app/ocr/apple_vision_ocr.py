"""Apple-oriented OCR engine scaffolding for LocalHomeApp.

Purpose:
- Provide the Apple-oriented OCR engine boundary through a macOS-native bridge.

Inputs:
- intake identifier
- local source artifact path

Outputs:
- structured OCR result record

Dependencies:
- pathlib
- time
- uuid
- apple_vision_bridge
- ocr_engine_interface
- ocr_result_models

Execution context:
- used on Apple hardware environments.

Required permissions:
- local file access
- macOS-native OCR bridge/runtime access when implemented

Expected errors/failure modes:
- bridge not yet implemented
- bridge execution failure

Related tests:
- tests/unit/test_apple_vision_ocr.py

Related docs:
- docs/modules/apple-vision-ocr.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

import time
from pathlib import Path
from uuid import uuid4

from local_home_app.ocr.apple_vision_bridge import run_apple_vision_bridge
from local_home_app.ocr.ocr_engine_interface import OcrEngineInterface
from local_home_app.ocr.ocr_result_models import OcrResultRecord


class AppleVisionOcrEngine(OcrEngineInterface):
    """Apple-oriented OCR engine using a macOS-native bridge boundary."""

    def run_ocr(self, *, intake_id: str, source_artifact_path: Path) -> OcrResultRecord:
        start = time.time()
        bridge_result = run_apple_vision_bridge(source_artifact_path)
        runtime_ms = int((time.time() - start) * 1000)

        if not bridge_result.success:
            return OcrResultRecord(
                ocr_run_id=str(uuid4()),
                intake_id=intake_id,
                engine_name="apple_vision",
                engine_version=None,
                source_artifact_path=str(source_artifact_path),
                preprocessed_artifact_path=None,
                ocr_text="",
                confidence_summary=None,
                runtime_ms=runtime_ms,
                status="not_available",
                error_message=bridge_result.error_message,
            )

        return OcrResultRecord(
            ocr_run_id=str(uuid4()),
            intake_id=intake_id,
            engine_name="apple_vision",
            engine_version=None,
            source_artifact_path=str(source_artifact_path),
            preprocessed_artifact_path=None,
            ocr_text=bridge_result.ocr_text,
            confidence_summary=None,
            runtime_ms=runtime_ms,
            status="completed",
            error_message=None,
        )
