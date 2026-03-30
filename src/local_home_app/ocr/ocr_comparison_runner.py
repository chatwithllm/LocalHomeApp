"""OCR comparison runner for LocalHomeApp.

Purpose:
- Run multiple OCR variants against a single artifact and package the results for comparison.

Inputs:
- intake identifier
- source artifact path
- OCR engine variants with labels

Outputs:
- structured OCR comparison record

Dependencies:
- uuid
- pathlib
- ocr_comparison_models
- ocr_engine_interface

Execution context:
- used by OCR comparison workflows for raw/preprocessed and future engine comparisons.

Required permissions:
- depends on selected OCR engine implementations.

Expected errors/failure modes:
- OCR engine execution failures
- invalid comparison configuration

Related tests:
- tests/unit/test_ocr_comparison_runner.py

Related docs:
- docs/modules/ocr-comparison-runner.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Tuple
from uuid import uuid4

from local_home_app.ocr.ocr_comparison_models import (
    OcrComparisonEntry,
    OcrComparisonRecord,
)
from local_home_app.ocr.ocr_engine_interface import OcrEngineInterface


def run_ocr_comparison(
    *,
    intake_id: str,
    source_artifact_path: Path,
    variants: Iterable[Tuple[str, OcrEngineInterface]],
) -> OcrComparisonRecord:
    """Run multiple OCR variants for comparison."""

    entries = []
    for label, engine in variants:
        result = engine.run_ocr(intake_id=intake_id, source_artifact_path=source_artifact_path)
        entries.append(OcrComparisonEntry(label=label, result=result))

    return OcrComparisonRecord(
        comparison_id=str(uuid4()),
        intake_id=intake_id,
        entries=entries,
    )
