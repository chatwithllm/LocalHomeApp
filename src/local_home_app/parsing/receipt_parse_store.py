"""Local receipt parse storage for LocalHomeApp.

Purpose:
- Persist structured receipt parse results locally in a simple file-backed format during early Phase 3.

Inputs:
- structured receipt parse records

Outputs:
- persisted and reloadable parse records

Dependencies:
- json
- dataclasses
- pathlib

Execution context:
- used by parsing runtime workflows before database-backed parse storage is introduced.

Required permissions:
- read/write access to local sensitive parse storage

Expected errors/failure modes:
- invalid JSONL content
- unwritable local storage path

Related tests:
- tests/unit/test_receipt_parse_store.py

Related docs:
- docs/modules/receipt-parse-store.md
- docs/phases/phase-03-receipt-parsing.md
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import List

from local_home_app.parsing.receipt_parse_models import ReceiptLineItemRecord, ReceiptParseRecord


class ReceiptParseStore:
    """Persist structured receipt parse records as JSONL."""

    def __init__(self, parses_file_path: Path) -> None:
        self.parses_file_path = parses_file_path
        self.parses_file_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, record: ReceiptParseRecord) -> None:
        with self.parses_file_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(record)) + "\n")

    def load_all(self) -> List[ReceiptParseRecord]:
        if not self.parses_file_path.exists():
            return []

        records: List[ReceiptParseRecord] = []
        with self.parses_file_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                payload = json.loads(line)
                line_items = [ReceiptLineItemRecord(**entry) for entry in payload.get("line_items", [])]
                payload["line_items"] = line_items
                records.append(ReceiptParseRecord(**payload))
        return records
