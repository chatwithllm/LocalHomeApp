"""Local file-backed intake metadata store for LocalHomeApp.

Purpose:
- Provide a simple Phase 1 local persistence layer for intake metadata.

Inputs:
- Intake event records.

Outputs:
- JSONL-backed persisted intake records.

Dependencies:
- json
- dataclasses
- pathlib

Execution context:
- Used by Phase 1 intake workflow before a database-backed store is implemented.

Required permissions:
- Read/write access to local sensitive storage root.

Expected errors/failure modes:
- Unwritable metadata file.
- Invalid JSONL content.

Related tests:
- tests/unit/test_local_intake_store.py

Related docs:
- docs/modules/local-intake-store.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import List

from local_home_app.ingestion.intake_event_store import IntakeEventRecord


class LocalIntakeStore:
    """Persist intake metadata as JSONL during early Phase 1."""

    def __init__(self, metadata_file_path: Path) -> None:
        self.metadata_file_path = metadata_file_path
        self.metadata_file_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, record: IntakeEventRecord) -> None:
        with self.metadata_file_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(record)) + "\n")

    def load_all(self) -> List[IntakeEventRecord]:
        if not self.metadata_file_path.exists():
            return []

        records: List[IntakeEventRecord] = []
        with self.metadata_file_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                payload = json.loads(line)
                records.append(IntakeEventRecord(**payload))
        return records
