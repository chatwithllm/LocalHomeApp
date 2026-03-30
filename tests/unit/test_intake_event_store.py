from local_home_app.ingestion.intake_event_store import IntakeEventRecord


def test_intake_event_record_fields() -> None:
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

    assert record.source_channel == "telegram"
    assert record.intake_status == "received"
