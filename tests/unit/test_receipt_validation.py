from local_home_app.ingestion.receipt_validation import validate_receipt_candidate
from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


def test_validate_receipt_candidate_accepts_jpeg() -> None:
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

    result = validate_receipt_candidate(candidate)
    assert result.accepted is True


def test_validate_receipt_candidate_rejects_text_file() -> None:
    candidate = TelegramReceiptCandidate(
        chat_id="5143357049",
        message_id="477",
        user_id="5143357049",
        media_type="document",
        file_id="abc123",
        file_unique_id="unique123",
        file_name="notes.txt",
        mime_type="text/plain",
        file_size_bytes=1024,
    )

    result = validate_receipt_candidate(candidate)
    assert result.accepted is False
    assert result.reason is not None
