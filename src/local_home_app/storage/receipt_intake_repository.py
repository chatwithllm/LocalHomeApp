"""Receipt intake repository for LocalHomeApp.

Purpose:
- Persist and retrieve receipt intake event records in SQLite.

Inputs:
- receipt intake event records

Outputs:
- stored and loaded receipt intake records

Dependencies:
- sqlite3
- intake_event_store

Execution context:
- used by storage workflows after intake processing.

Required permissions:
- read/write access to local database

Expected errors/failure modes:
- insert or query failures

Related tests:
- tests/unit/test_receipt_intake_repository.py

Related docs:
- docs/modules/receipt-intake-repository.md
- docs/phases/phase-04-local-storage.md
"""

from __future__ import annotations

import sqlite3
from typing import Optional

from local_home_app.ingestion.intake_event_store import IntakeEventRecord


class ReceiptIntakeRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def insert(self, record: IntakeEventRecord) -> None:
        self.connection.execute(
            """
            INSERT INTO receipt_intake_events (
                intake_id, source_channel, source_account_id, telegram_chat_id,
                telegram_message_id, telegram_user_id, telegram_file_id,
                telegram_file_unique_id, stored_at_path, media_type, mime_type,
                file_size_bytes, sha256, intake_status, duplicate_of_intake_id, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record.intake_id,
                record.source_channel,
                record.source_account_id,
                record.telegram_chat_id,
                record.telegram_message_id,
                record.telegram_user_id,
                record.telegram_file_id,
                record.telegram_file_unique_id,
                record.stored_at_path,
                record.media_type,
                record.mime_type,
                record.file_size_bytes,
                record.sha256,
                record.intake_status,
                record.duplicate_of_intake_id,
                record.notes,
            ),
        )
        self.connection.commit()

    def get_by_id(self, intake_id: str) -> Optional[sqlite3.Row]:
        cursor = self.connection.execute(
            "SELECT * FROM receipt_intake_events WHERE intake_id = ?",
            (intake_id,),
        )
        return cursor.fetchone()
