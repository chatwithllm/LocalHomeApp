"""Receipt parse repository for LocalHomeApp.

Purpose:
- Persist and retrieve structured receipt parse records and line items in SQLite.

Inputs:
- structured receipt parse records

Outputs:
- stored and loaded parse records

Dependencies:
- sqlite3
- receipt_parse_models

Execution context:
- used after receipt parsing.

Required permissions:
- read/write access to local database

Expected errors/failure modes:
- insert or query failures

Related tests:
- tests/unit/test_receipt_parse_repository.py

Related docs:
- docs/modules/receipt-parse-repository.md
- docs/phases/phase-04-local-storage.md
"""

from __future__ import annotations

import sqlite3
from typing import Optional

from local_home_app.parsing.receipt_parse_models import ReceiptParseRecord


class ReceiptParseRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def insert(self, record: ReceiptParseRecord) -> None:
        self.connection.execute(
            """
            INSERT INTO receipt_parses (
                parse_id, intake_id, ocr_run_id, merchant_name, receipt_date,
                receipt_time, subtotal, tax, total, payment_method_summary,
                currency, parse_status, confidence_summary, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record.parse_id,
                record.intake_id,
                record.ocr_run_id,
                record.merchant_name,
                record.receipt_date,
                record.receipt_time,
                record.subtotal,
                record.tax,
                record.total,
                record.payment_method_summary,
                record.currency,
                record.parse_status,
                record.confidence_summary,
                record.notes,
            ),
        )
        for item in record.line_items:
            self.connection.execute(
                """
                INSERT INTO receipt_line_items (
                    line_id, parse_id, raw_text, item_name, quantity,
                    unit_price, line_total, discount_text, confidence_summary
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item.line_id,
                    item.parse_id,
                    item.raw_text,
                    item.item_name,
                    item.quantity,
                    item.unit_price,
                    item.line_total,
                    item.discount_text,
                    item.confidence_summary,
                ),
            )
        self.connection.commit()

    def get_by_id(self, parse_id: str) -> Optional[sqlite3.Row]:
        cursor = self.connection.execute(
            "SELECT * FROM receipt_parses WHERE parse_id = ?",
            (parse_id,),
        )
        return cursor.fetchone()
