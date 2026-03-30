from pathlib import Path

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.config.application_settings import ApplicationSettings
from local_home_app.ingestion.intake_orchestrator import process_local_receipt_intake
from local_home_app.ingestion.local_intake_store import LocalIntakeStore
from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


def test_process_local_receipt_intake(tmp_path: Path) -> None:
    settings = ApplicationSettings(
        data_root=str(tmp_path),
        database_path=str(tmp_path / "database" / "local_home_app.sqlite"),
    )
    paths = FileSystemPaths(settings)
    store = LocalIntakeStore(tmp_path / "metadata" / "intake.jsonl")
    candidate = TelegramReceiptCandidate(
        chat_id="5143357049",
        message_id="477",
        user_id="5143357049",
        media_type="photo",
        file_id="abc123",
        file_unique_id="unique123",
        file_name="receipt.jpg",
        mime_type="image/jpeg",
        file_size_bytes=1024,
    )

    result = process_local_receipt_intake(
        candidate=candidate,
        file_bytes=b"receipt-bytes",
        paths=paths,
        store=store,
    )

    assert result.record.intake_status == "received"
    assert result.duplicate_of is None
    assert result.stored_file_path.exists()


def test_process_local_receipt_intake_marks_duplicate(tmp_path: Path) -> None:
    settings = ApplicationSettings(
        data_root=str(tmp_path),
        database_path=str(tmp_path / "database" / "local_home_app.sqlite"),
    )
    paths = FileSystemPaths(settings)
    store = LocalIntakeStore(tmp_path / "metadata" / "intake.jsonl")
    candidate = TelegramReceiptCandidate(
        chat_id="5143357049",
        message_id="477",
        user_id="5143357049",
        media_type="photo",
        file_id="abc123",
        file_unique_id="unique123",
        file_name="receipt.jpg",
        mime_type="image/jpeg",
        file_size_bytes=1024,
    )

    first = process_local_receipt_intake(
        candidate=candidate,
        file_bytes=b"receipt-bytes",
        paths=paths,
        store=store,
    )
    second = process_local_receipt_intake(
        candidate=candidate,
        file_bytes=b"receipt-bytes",
        paths=paths,
        store=store,
    )

    assert first.record.intake_status == "received"
    assert second.record.intake_status == "duplicate"
    assert second.record.duplicate_of_intake_id == first.record.intake_id
