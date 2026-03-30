"""OCR comparison models for LocalHomeApp.

Purpose:
- Represent structured comparison results between multiple OCR runs.

Inputs:
- OCR result records from different engine/preprocessing variants.

Outputs:
- structured OCR comparison records.

Dependencies:
- dataclasses
- typing

Execution context:
- used by OCR comparison workflows.

Required permissions:
- none directly.

Expected errors/failure modes:
- missing comparison labels or OCR references.

Related tests:
- tests/unit/test_ocr_comparison_models.py

Related docs:
- docs/modules/ocr-comparison-models.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from local_home_app.ocr.ocr_result_models import OcrResultRecord


@dataclass(frozen=True)
class OcrComparisonEntry:
    label: str
    result: OcrResultRecord


@dataclass(frozen=True)
class OcrComparisonRecord:
    comparison_id: str
    intake_id: str
    entries: List[OcrComparisonEntry]
