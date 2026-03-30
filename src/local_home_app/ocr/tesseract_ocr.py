"""Portable Tesseract OCR engine scaffolding for LocalHomeApp.

Purpose:
- Provide the portable OCR engine boundary for Tesseract-based implementation.

Inputs:
- intake identifier
- local source artifact path

Outputs:
- structured OCR result record

Dependencies:
- pathlib
- shutil
- subprocess
- time
- uuid
- ocr_engine_interface
- ocr_result_models

Execution context:
- used on portable/local environments where Tesseract is installed.

Required permissions:
- local file access
- local process execution

Expected errors/failure modes:
- tesseract not installed
- OCR command failure

Related tests:
- tests/unit/test_tesseract_ocr.py

Related docs:
- docs/modules/tesseract-ocr.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

import shutil
import subprocess
import time
from pathlib import Path
from uuid import uuid4

from local_home_app.ocr.ocr_engine_interface import OcrEngineInterface
from local_home_app.ocr.ocr_result_models import OcrResultRecord
from local_home_app.ocr.receipt_image_preprocessor import prepare_receipt_image_for_ocr


class TesseractOcrEngine(OcrEngineInterface):
    """Portable Tesseract OCR engine implementation."""

    def __init__(
        self,
        binary_name: str = "tesseract",
        preprocess: bool = True,
        preprocessed_output_dir: Path | None = None,
    ) -> None:
        self.binary_name = binary_name
        self.preprocess = preprocess
        self.preprocessed_output_dir = preprocessed_output_dir

    def run_ocr(self, *, intake_id: str, source_artifact_path: Path) -> OcrResultRecord:
        start = time.time()

        artifact_for_ocr = source_artifact_path
        preprocessed_artifact_path = None
        if self.preprocess:
            artifact_for_ocr = prepare_receipt_image_for_ocr(
                source_artifact_path,
                destination_dir=self.preprocessed_output_dir,
            )
            if artifact_for_ocr != source_artifact_path:
                preprocessed_artifact_path = str(artifact_for_ocr)

        binary_path = shutil.which(self.binary_name)
        if binary_path is None:
            return OcrResultRecord(
                ocr_run_id=str(uuid4()),
                intake_id=intake_id,
                engine_name="tesseract",
                engine_version=None,
                source_artifact_path=str(source_artifact_path),
                preprocessed_artifact_path=preprocessed_artifact_path,
                ocr_text="",
                confidence_summary=None,
                runtime_ms=None,
                status="not_available",
                error_message="Tesseract binary not found",
            )

        completed = subprocess.run(
            [binary_path, str(artifact_for_ocr), "stdout"],
            capture_output=True,
            text=True,
            check=False,
        )
        runtime_ms = int((time.time() - start) * 1000)

        if completed.returncode != 0:
            return OcrResultRecord(
                ocr_run_id=str(uuid4()),
                intake_id=intake_id,
                engine_name="tesseract",
                engine_version=None,
                source_artifact_path=str(source_artifact_path),
                preprocessed_artifact_path=preprocessed_artifact_path,
                ocr_text="",
                confidence_summary=None,
                runtime_ms=runtime_ms,
                status="failed",
                error_message=completed.stderr.strip() or "Tesseract execution failed",
            )

        return OcrResultRecord(
            ocr_run_id=str(uuid4()),
            intake_id=intake_id,
            engine_name="tesseract",
            engine_version=None,
            source_artifact_path=str(source_artifact_path),
            preprocessed_artifact_path=preprocessed_artifact_path,
            ocr_text=completed.stdout,
            confidence_summary=None,
            runtime_ms=runtime_ms,
            status="completed",
            error_message=None,
        )
