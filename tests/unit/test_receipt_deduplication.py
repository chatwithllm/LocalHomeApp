from local_home_app.ingestion.intake_event_store import IntakeEventRecord
from local_home_app.ingestion.receipt_deduplication import find_duplicate_intake_event


def test_find_duplicate_by_file_unique_id() -> None:
    existing = [
        IntakeEventRecord(
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
    ]

    duplicate = find_duplicate_intake_event(
        telegram_file_unique_id="unique123",
        sha256=None,
        existing_records=existing,
    )

    assert duplicate is not None
    assert duplicate.intake_id == "intake-001"
