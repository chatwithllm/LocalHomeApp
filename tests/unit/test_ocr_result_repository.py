from pathlib import Path

from local_home_app.ocr.ocr_result_models import OcrResultRecord
from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.database_migration_runner import run_migrations
from local_home_app.storage.ocr_result_repository import OcrResultRepository


def test_ocr_result_repository_insert_and_get(tmp_path: Path) -> None:
    connection = create_database_connection(tmp_path / "local_home_app.sqlite")
    try:
        run_migrations(connection)
        connection.execute(
            "INSERT INTO receipt_intake_events (intake_id, source_channel, source_account_id, stored_at_path, media_type, intake_status) VALUES (?, ?, ?, ?, ?, ?)",
            ("intake-001", "telegram", "default", "/tmp/receipt.jpg", "photo", "received"),
        )
        connection.commit()
        repository = OcrResultRepository(connection)
        record = OcrResultRecord(
            ocr_run_id="ocr-001",
            intake_id="intake-001",
            engine_name="tesseract",
            engine_version=None,
            source_artifact_path="/tmp/receipt.jpg",
            preprocessed_artifact_path=None,
            ocr_text="TOTAL 39.04",
            confidence_summary=None,
            runtime_ms=100,
            status="completed",
        )
        repository.insert(record)
        stored = repository.get_by_id("ocr-001")
        assert stored is not None
        assert stored['engine_name'] == 'tesseract'
    finally:
        connection.close()
