"""OCR runtime service scaffolding for LocalHomeApp.

Purpose:
- Provide a simple orchestration entry point for OCR engine execution.

Inputs:
- OCR engine implementation
- intake identifier
- source artifact path

Outputs:
- OCR result record

Dependencies:
- pathlib
- ocr_engine_interface
- ocr_result_models

Execution context:
- used by later OCR workflow layers.

Required permissions:
- depends on selected OCR engine implementation.

Expected errors/failure modes:
- engine execution failure.

Related tests:
- tests/unit/test_ocr_runtime_service.py

Related docs:
- docs/modules/ocr-runtime-service.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

from pathlib import Path

from local_home_app.ocr.ocr_engine_interface import OcrEngineInterface
from local_home_app.ocr.ocr_result_models import OcrResultRecord


def run_ocr_for_artifact(
    *, engine: OcrEngineInterface, intake_id: str, source_artifact_path: Path
) -> OcrResultRecord:
    """Run OCR through the configured engine interface."""

    return engine.run_ocr(intake_id=intake_id, source_artifact_path=source_artifact_path)
