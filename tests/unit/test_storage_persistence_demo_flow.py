from pathlib import Path

from local_home_app.ingestion.intake_event_store import IntakeEventRecord
from local_home_app.ocr.ocr_result_models import OcrResultRecord
from local_home_app.parsing.receipt_parse_runtime_service import run_receipt_parse
from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.database_migration_runner import run_migrations
from local_home_app.storage.ocr_result_repository import OcrResultRepository
from local_home_app.storage.purchase_history_repository import PurchaseHistoryRepository
from local_home_app.storage.receipt_intake_repository import ReceiptIntakeRepository
from local_home_app.storage.receipt_parse_repository import ReceiptParseRepository


def test_storage_persistence_demo_flow(tmp_path: Path) -> None:
    database_path = tmp_path / 'local_home_app.sqlite'
    connection = create_database_connection(database_path)
    try:
        run_migrations(connection)
        intake = IntakeEventRecord(
            intake_id='demo-intake-001',
            source_channel='telegram',
            source_account_id='default',
            telegram_chat_id='5143357049',
            telegram_message_id='demo-msg-001',
            telegram_user_id='5143357049',
            telegram_file_id='demo-file-001',
            telegram_file_unique_id='demo-unique-001',
            stored_at_path='/tmp/demo-receipt.jpg',
            media_type='photo',
            mime_type='image/jpeg',
            file_size_bytes=1234,
            sha256='demo-hash-001',
            intake_status='received',
        )
        ReceiptIntakeRepository(connection).insert(intake)

        fixture_text = Path('tests/fixtures/kroger_ocr_sample.txt').read_text(encoding='utf-8')
        ocr = OcrResultRecord(
            ocr_run_id='demo-ocr-001',
            intake_id='demo-intake-001',
            engine_name='tesseract',
            engine_version='5.5.2',
            source_artifact_path='/tmp/demo-receipt.jpg',
            preprocessed_artifact_path=None,
            ocr_text=fixture_text,
            confidence_summary=None,
            runtime_ms=100,
            status='completed',
        )
        OcrResultRepository(connection).insert(ocr)

        parse = run_receipt_parse(
            intake_id='demo-intake-001',
            ocr_run_id='demo-ocr-001',
            ocr_text=fixture_text,
        )
        ReceiptParseRepository(connection).insert(parse)

        rows = PurchaseHistoryRepository(connection).list_line_items()
        assert len(rows) > 0
        assert any(row['merchant_name'] == 'Kroger' for row in rows)
    finally:
        connection.close()
