"""Local OCR result storage for LocalHomeApp.

Purpose:
- Persist OCR results locally in a simple file-backed format during early Phase 2.

Inputs:
- OCR result records

Outputs:
- persisted and reloadable OCR result records

Dependencies:
- json
- dataclasses
- pathlib

Execution context:
- used by OCR runtime workflows before a database-backed OCR store is introduced.

Required permissions:
- read/write access to local sensitive OCR storage

Expected errors/failure modes:
- invalid JSONL content
- unwritable local storage path

Related tests:
- tests/unit/test_ocr_result_store.py

Related docs:
- docs/modules/ocr-result-store.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import List

from local_home_app.ocr.ocr_result_models import OcrResultRecord


class OcrResultStore:
    """Persist OCR results as JSONL during early Phase 2."""

    def __init__(self, results_file_path: Path) -> None:
        self.results_file_path = results_file_path
        self.results_file_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, record: OcrResultRecord) -> None:
        with self.results_file_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(record)) + "\n")

    def load_all(self) -> List[OcrResultRecord]:
        if not self.results_file_path.exists():
            return []

        records: List[OcrResultRecord] = []
        with self.results_file_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                payload = json.loads(line)
                records.append(OcrResultRecord(**payload))
        return records
