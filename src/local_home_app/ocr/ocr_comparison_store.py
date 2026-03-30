"""Local OCR comparison storage for LocalHomeApp.

Purpose:
- Persist OCR comparison results locally in a simple file-backed format.

Inputs:
- OCR comparison records

Outputs:
- persisted and reloadable OCR comparison records

Dependencies:
- json
- dataclasses
- pathlib

Execution context:
- used by OCR comparison workflows.

Required permissions:
- read/write access to local sensitive OCR storage

Expected errors/failure modes:
- invalid JSONL content
- unwritable local storage path

Related tests:
- tests/unit/test_ocr_comparison_store.py

Related docs:
- docs/modules/ocr-comparison-store.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import List

from local_home_app.ocr.ocr_comparison_models import OcrComparisonRecord


class OcrComparisonStore:
    """Persist OCR comparison records as JSONL."""

    def __init__(self, comparisons_file_path: Path) -> None:
        self.comparisons_file_path = comparisons_file_path
        self.comparisons_file_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, record: OcrComparisonRecord) -> None:
        with self.comparisons_file_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(record)) + "\n")

    def load_all(self) -> List[OcrComparisonRecord]:
        if not self.comparisons_file_path.exists():
            return []

        records: List[OcrComparisonRecord] = []
        with self.comparisons_file_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                payload = json.loads(line)
                entries = payload["entries"]
                records.append(OcrComparisonRecord(comparison_id=payload["comparison_id"], intake_id=payload["intake_id"], entries=entries))
        return records
