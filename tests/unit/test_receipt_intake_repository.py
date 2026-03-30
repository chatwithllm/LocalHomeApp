from pathlib import Path

from local_home_app.ingestion.intake_event_store import IntakeEventRecord
from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.database_migration_runner import run_migrations
from local_home_app.storage.receipt_intake_repository import ReceiptIntakeRepository


def test_receipt_intake_repository_insert_and_get(tmp_path: Path) -> None:
    connection = create_database_connection(tmp_path / "local_home_app.sqlite")
    try:
        run_migrations(connection)
        repository = ReceiptIntakeRepository(connection)
        record = IntakeEventRecord(
            intake_id="intake-001",
            source_channel="telegram",
            source_account_id="default",
            telegram_chat_id="chat-1",
            telegram_message_id="msg-1",
            telegram_user_id="user-1",
            telegram_file_id="file-1",
            telegram_file_unique_id="unique-1",
            stored_at_path="/tmp/receipt.jpg",
            media_type="photo",
            mime_type="image/jpeg",
            file_size_bytes=1024,
            sha256="hash123",
            intake_status="received",
        )
        repository.insert(record)
        stored = repository.get_by_id("intake-001")
        assert stored is not None
        assert stored['source_channel'] == 'telegram'
    finally:
        connection.close()
