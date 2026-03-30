from local_home_app.ingestion.intake_event_store import IntakeEventRecord
from local_home_app.ingestion.intake_events import (
    format_alert_validation_message,
    format_worker_intake_message,
)
from local_home_app.ingestion.receipt_validation import ReceiptValidationResult


def test_format_worker_intake_message() -> None:
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
        intake_status="stored",
    )

    message = format_worker_intake_message(record)
    assert "stored" in message
    assert "intake-001" in message


def test_format_alert_validation_message() -> None:
    validation = ReceiptValidationResult(accepted=False, reason="Unsupported mime type")
    message = format_alert_validation_message(
        candidate_chat_id="5143357049",
        candidate_message_id="477",
        validation=validation,
    )
    assert "validation failed" in message
    assert "Unsupported mime type" in message
