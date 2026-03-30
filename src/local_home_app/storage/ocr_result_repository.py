"""OCR result repository for LocalHomeApp.

Purpose:
- Persist and retrieve OCR result records in SQLite.

Inputs:
- OCR result records

Outputs:
- stored and loaded OCR result records

Dependencies:
- sqlite3
- ocr_result_models

Execution context:
- used after OCR execution.

Required permissions:
- read/write access to local database

Expected errors/failure modes:
- insert or query failures

Related tests:
- tests/unit/test_ocr_result_repository.py

Related docs:
- docs/modules/ocr-result-repository.md
- docs/phases/phase-04-local-storage.md
"""

from __future__ import annotations

import sqlite3
from typing import Optional

from local_home_app.ocr.ocr_result_models import OcrResultRecord


class OcrResultRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def insert(self, record: OcrResultRecord) -> None:
        self.connection.execute(
            """
            INSERT INTO ocr_results (
                ocr_run_id, intake_id, engine_name, engine_version,
                source_artifact_path, preprocessed_artifact_path, ocr_text,
                confidence_summary, runtime_ms, status, error_message
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record.ocr_run_id,
                record.intake_id,
                record.engine_name,
                record.engine_version,
                record.source_artifact_path,
                record.preprocessed_artifact_path,
                record.ocr_text,
                record.confidence_summary,
                record.runtime_ms,
                record.status,
                record.error_message,
            ),
        )
        self.connection.commit()

    def get_by_id(self, ocr_run_id: str) -> Optional[sqlite3.Row]:
        cursor = self.connection.execute(
            "SELECT * FROM ocr_results WHERE ocr_run_id = ?",
            (ocr_run_id,),
        )
        return cursor.fetchone()
