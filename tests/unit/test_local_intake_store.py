from pathlib import Path

from local_home_app.ingestion.intake_event_store import IntakeEventRecord
from local_home_app.ingestion.local_intake_store import LocalIntakeStore


def test_local_intake_store_append_and_load(tmp_path: Path) -> None:
    store = LocalIntakeStore(tmp_path / "intake.jsonl")
    record = IntakeEventRecord(
        intake_id="intake-001",
        source_channel="telegram",
        source_account_id="default",
        telegram_chat_id="5143357049",
        telegram_message_id="477",
        telegram_user_id="5143357049",
        telegram_file_id="abc123",
        telegram_file_unique_id="unique123",
        stored_at_path="/tmp/receipt.jpg",
        media_type="photo",
        mime_type="image/jpeg",
        file_size_bytes=1024,
        sha256="hash123",
        intake_status="received",
    )

    store.append(record)
    loaded = store.load_all()

    assert len(loaded) == 1
    assert loaded[0].intake_id == "intake-001"
