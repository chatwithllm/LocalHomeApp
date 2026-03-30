from pathlib import Path

from local_home_app.ingestion.intake_workflow import build_intake_event_record
from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


def test_build_intake_event_record() -> None:
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

    record = build_intake_event_record(
        candidate=candidate,
        stored_at_path=Path("/tmp/receipt.jpg"),
        sha256="hash123",
    )

    assert record.source_channel == "telegram"
    assert record.sha256 == "hash123"
    assert record.stored_at_path == "/tmp/receipt.jpg"
