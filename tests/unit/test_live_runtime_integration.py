from pathlib import Path

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.config.application_settings import ApplicationSettings
from local_home_app.ingestion.live_runtime_integration import handle_telegram_update_for_intake
from local_home_app.ingestion.local_intake_store import LocalIntakeStore


class FakeTelegramBotClient:
    def get_file_path(self, file_id: str) -> str:
        return f"receipts/{file_id}.jpg"

    def download_file_bytes(self, file_path: str) -> bytes:
        return b"downloaded-receipt-bytes"


def test_handle_telegram_update_for_intake_returns_outputs(tmp_path: Path) -> None:
    settings = ApplicationSettings(
        data_root=str(tmp_path),
        database_path=str(tmp_path / "database" / "local_home_app.sqlite"),
    )
    paths = FileSystemPaths(settings)
    store = LocalIntakeStore(tmp_path / "metadata" / "intake.jsonl")

    outputs = handle_telegram_update_for_intake(
        update={
            "message": {
                "message_id": 477,
                "chat": {"id": 5143357049},
                "from": {"id": 5143357049},
                "photo": [
                    {"file_id": "small", "file_unique_id": "u1", "file_size": 100},
                    {"file_id": "large", "file_unique_id": "u2", "file_size": 200},
                ],
            }
        },
        paths=paths,
        store=store,
        bot_client=FakeTelegramBotClient(),
    )

    assert outputs is not None
    assert outputs.main_message is not None
    assert outputs.worker_message is not None


def test_handle_telegram_update_for_intake_non_receipt_returns_none(tmp_path: Path) -> None:
    settings = ApplicationSettings(
        data_root=str(tmp_path),
        database_path=str(tmp_path / "database" / "local_home_app.sqlite"),
    )
    paths = FileSystemPaths(settings)
    store = LocalIntakeStore(tmp_path / "metadata" / "intake.jsonl")

    outputs = handle_telegram_update_for_intake(
        update={
            "message": {
                "message_id": 478,
                "chat": {"id": 5143357049},
                "from": {"id": 5143357049},
                "text": "hello",
            }
        },
        paths=paths,
        store=store,
        bot_client=FakeTelegramBotClient(),
    )

    assert outputs is None
