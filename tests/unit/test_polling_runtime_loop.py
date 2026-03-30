from pathlib import Path

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.config.application_settings import ApplicationSettings
from local_home_app.ingestion.local_intake_store import LocalIntakeStore
from local_home_app.ingestion.polling_runtime_loop import process_polled_updates


class FakeTelegramUpdatesApi:
    def get_updates(self, *, offset=None, timeout=0):
        return [
            {
                "update_id": 1001,
                "message": {
                    "message_id": 477,
                    "chat": {"id": 5143357049},
                    "from": {"id": 5143357049},
                    "photo": [
                        {"file_id": "small", "file_unique_id": "u1", "file_size": 100},
                        {"file_id": "large", "file_unique_id": "u2", "file_size": 200},
                    ],
                },
            },
            {
                "update_id": 1002,
                "message": {
                    "message_id": 478,
                    "chat": {"id": 5143357049},
                    "from": {"id": 5143357049},
                    "text": "hello",
                },
            },
        ]


class FakeTelegramBotClient:
    def get_file_path(self, file_id: str) -> str:
        return f"receipts/{file_id}.jpg"

    def download_file_bytes(self, file_path: str) -> bytes:
        return b"downloaded-receipt-bytes"


def test_process_polled_updates(tmp_path: Path) -> None:
    settings = ApplicationSettings(
        data_root=str(tmp_path),
        database_path=str(tmp_path / "database" / "local_home_app.sqlite"),
    )
    paths = FileSystemPaths(settings)
    store = LocalIntakeStore(tmp_path / "metadata" / "intake.jsonl")

    result = process_polled_updates(
        updates_api=FakeTelegramUpdatesApi(),
        paths=paths,
        store=store,
        bot_client=FakeTelegramBotClient(),
        offset=None,
        timeout=0,
    )

    assert result.next_offset == 1003
    assert len(result.delivery_payloads) >= 2
