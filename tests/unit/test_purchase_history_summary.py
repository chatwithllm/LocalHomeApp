from pathlib import Path

from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.database_migration_runner import run_migrations
from local_home_app.storage.purchase_history_repository import PurchaseHistoryRepository


def test_purchase_history_repository_summarize_recent_receipts(tmp_path: Path) -> None:
    connection = create_database_connection(tmp_path / "local_home_app.sqlite")
    try:
        run_migrations(connection)
        connection.execute(
            "INSERT INTO receipt_intake_events (intake_id, source_channel, source_account_id, stored_at_path, media_type, intake_status) VALUES (?, ?, ?, ?, ?, ?)",
            ("intake-001", "telegram", "default", "/tmp/receipt.jpg", "photo", "received"),
        )
        connection.execute(
            "INSERT INTO ocr_results (ocr_run_id, intake_id, engine_name, source_artifact_path, ocr_text, status) VALUES (?, ?, ?, ?, ?, ?)",
            ("ocr-001", "intake-001", "tesseract", "/tmp/receipt.jpg", "TOTAL 39.04", "completed"),
        )
        connection.execute(
            "INSERT INTO receipt_parses (parse_id, intake_id, ocr_run_id, merchant_name, receipt_date, total, parse_status) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("parse-001", "intake-001", "ocr-001", "Kroger", "03/15/26", 39.04, "completed"),
        )
        connection.execute(
            "INSERT INTO receipt_line_items (line_id, parse_id, raw_text, item_name, line_total) VALUES (?, ?, ?, ?, ?)",
            ("line-001", "parse-001", "MILK 3.99", "MILK", 3.99),
        )
        connection.commit()

        rows = PurchaseHistoryRepository(connection).summarize_recent_receipts()
        assert len(rows) == 1
        assert rows[0]['merchant_name'] == 'Kroger'
        assert rows[0]['line_item_count'] == 1
    finally:
        connection.close()
