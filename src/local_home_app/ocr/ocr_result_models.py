"""OCR result models for LocalHomeApp.

Purpose:
- Represent OCR run outputs and metadata with clear provenance.

Inputs:
- OCR engine outputs and execution metadata.

Outputs:
- structured OCR result records.

Dependencies:
- dataclasses
- typing

Execution context:
- used by OCR runtime and storage components.

Required permissions:
- none directly.

Expected errors/failure modes:
- missing required provenance fields.

Related tests:
- tests/unit/test_ocr_result_models.py

Related docs:
- docs/modules/ocr-result-models.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class OcrResultRecord:
    ocr_run_id: str
    intake_id: str
    engine_name: str
    engine_version: Optional[str]
    source_artifact_path: str
    preprocessed_artifact_path: Optional[str]
    ocr_text: str
    confidence_summary: Optional[str]
    runtime_ms: Optional[int]
    status: str
    error_message: Optional[str] = None
