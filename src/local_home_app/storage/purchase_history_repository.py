"""Purchase history repository for LocalHomeApp.

Purpose:
- Provide query access to stored parsed receipt line items for household purchase history.

Inputs:
- query filters as needed later

Outputs:
- purchase history rows

Dependencies:
- sqlite3

Execution context:
- used by later analytics, signal, and recommendation phases.

Required permissions:
- read access to local database

Expected errors/failure modes:
- query failures

Related tests:
- tests/unit/test_purchase_history_repository.py

Related docs:
- docs/modules/purchase-history-repository.md
- docs/phases/phase-04-local-storage.md
"""

from __future__ import annotations

import sqlite3
from typing import List


class PurchaseHistoryRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def list_line_items(self) -> List[sqlite3.Row]:
        cursor = self.connection.execute(
            """
            SELECT rp.merchant_name, rp.receipt_date, rli.item_name, rli.line_total
            FROM receipt_line_items rli
            JOIN receipt_parses rp ON rp.parse_id = rli.parse_id
            ORDER BY rp.receipt_date, rp.parse_id
            """
        )
        return cursor.fetchall()

    def summarize_recent_receipts(self) -> List[sqlite3.Row]:
        cursor = self.connection.execute(
            """
            SELECT
                rp.merchant_name,
                rp.receipt_date,
                rp.total,
                COUNT(rli.line_id) AS line_item_count
            FROM receipt_parses rp
            LEFT JOIN receipt_line_items rli ON rli.parse_id = rp.parse_id
            GROUP BY rp.parse_id, rp.merchant_name, rp.receipt_date, rp.total
            ORDER BY rp.receipt_date DESC, rp.parse_id DESC
            """
        )
        return cursor.fetchall()
