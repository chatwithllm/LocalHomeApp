"""OCR engine interface for LocalHomeApp.

Purpose:
- Define the common interface that all OCR engine implementations must follow.

Inputs:
- local source artifact path
- intake provenance identifiers

Outputs:
- structured OCR result records

Dependencies:
- abc
- pathlib
- ocr_result_models

Execution context:
- implemented by engine-specific OCR modules.

Required permissions:
- engine implementations may require local file/process access.

Expected errors/failure modes:
- engine-specific runtime failures.

Related tests:
- tests/unit/test_ocr_engine_interface.py

Related docs:
- docs/modules/ocr-engine-interface.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from local_home_app.ocr.ocr_result_models import OcrResultRecord


class OcrEngineInterface(ABC):
    """Common interface for OCR engines used by LocalHomeApp."""

    @abstractmethod
    def run_ocr(self, *, intake_id: str, source_artifact_path: Path) -> OcrResultRecord:
        """Run OCR against a local receipt artifact and return a structured result."""
