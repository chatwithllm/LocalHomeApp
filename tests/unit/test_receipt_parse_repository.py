from pathlib import Path

from local_home_app.parsing.receipt_parse_models import ReceiptLineItemRecord, ReceiptParseRecord
from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.database_migration_runner import run_migrations
from local_home_app.storage.receipt_parse_repository import ReceiptParseRepository


def test_receipt_parse_repository_insert_and_get(tmp_path: Path) -> None:
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
        connection.commit()
        repository = ReceiptParseRepository(connection)
        record = ReceiptParseRecord(
            parse_id="parse-001",
            intake_id="intake-001",
            ocr_run_id="ocr-001",
            merchant_name="Kroger",
            receipt_date="03/15/26",
            receipt_time="01:21pm",
            subtotal=None,
            tax=None,
            total=39.04,
            payment_method_summary="VISA",
            currency="USD",
            parse_status="completed",
            confidence_summary="medium",
            notes=None,
            line_items=[
                ReceiptLineItemRecord(
                    line_id="line-001",
                    parse_id="parse-001",
                    raw_text="MILK 3.99",
                    item_name="MILK",
                    quantity=None,
                    unit_price=None,
                    line_total=3.99,
                    discount_text=None,
                    confidence_summary="medium",
                )
            ],
        )
        repository.insert(record)
        stored = repository.get_by_id("parse-001")
        assert stored is not None
        assert stored['merchant_name'] == 'Kroger'
    finally:
        connection.close()
