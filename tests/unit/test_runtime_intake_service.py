from pathlib import Path

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.common.runtime_errors import TelegramIntegrationError
from local_home_app.config.application_settings import ApplicationSettings
from local_home_app.ingestion.local_intake_store import LocalIntakeStore
from local_home_app.ingestion.runtime_intake_service import process_telegram_candidate_via_bot
from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


class FakeTelegramBotClient:
    def get_file_path(self, file_id: str) -> str:
        return f"receipts/{file_id}.jpg"

    def download_file_bytes(self, file_path: str) -> bytes:
        return b"downloaded-receipt-bytes"


class FailingTelegramBotClient:
    def get_file_path(self, file_id: str) -> str:
        raise TelegramIntegrationError("download failed")

    def download_file_bytes(self, file_path: str) -> bytes:
        raise AssertionError("should not reach download when get_file_path fails")


def test_process_telegram_candidate_via_bot(tmp_path: Path) -> None:
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

    result = process_telegram_candidate_via_bot(
        candidate=candidate,
        paths=paths,
        store=store,
        bot_client=FakeTelegramBotClient(),
    )

    assert result.record is not None
    assert result.record.intake_status == "received"
    assert result.worker_message is not None
    assert result.alert_message is None
    assert result.stored_file_path is not None
    assert result.stored_file_path.exists()


def test_process_telegram_candidate_via_bot_rejects_invalid_candidate(tmp_path: Path) -> None:
    settings = ApplicationSettings(
        data_root=str(tmp_path),
        database_path=str(tmp_path / "database" / "local_home_app.sqlite"),
    )
    paths = FileSystemPaths(settings)
    store = LocalIntakeStore(tmp_path / "metadata" / "intake.jsonl")
    candidate = TelegramReceiptCandidate(
        chat_id="5143357049",
        message_id="478",
        user_id="5143357049",
        media_type="document",
        file_id="abc124",
        file_unique_id="unique124",
        file_name="notes.txt",
        mime_type="text/plain",
        file_size_bytes=256,
    )

    result = process_telegram_candidate_via_bot(
        candidate=candidate,
        paths=paths,
        store=store,
        bot_client=FakeTelegramBotClient(),
    )

    assert result.record is None
    assert result.worker_message is None
    assert result.alert_message is not None
    assert result.stored_file_path is None


def test_process_telegram_candidate_via_bot_handles_download_failure(tmp_path: Path) -> None:
    settings = ApplicationSettings(
        data_root=str(tmp_path),
        database_path=str(tmp_path / "database" / "local_home_app.sqlite"),
    )
    paths = FileSystemPaths(settings)
    store = LocalIntakeStore(tmp_path / "metadata" / "intake.jsonl")
    candidate = TelegramReceiptCandidate(
        chat_id="5143357049",
        message_id="479",
        user_id="5143357049",
        media_type="photo",
        file_id="abc125",
        file_unique_id="unique125",
        file_name="receipt.jpg",
        mime_type="image/jpeg",
        file_size_bytes=1024,
    )

    result = process_telegram_candidate_via_bot(
        candidate=candidate,
        paths=paths,
        store=store,
        bot_client=FailingTelegramBotClient(),
    )

    assert result.record is None
    assert result.worker_message is None
    assert result.alert_message is not None
    assert "failed_download" in result.alert_message
    assert result.stored_file_path is None
