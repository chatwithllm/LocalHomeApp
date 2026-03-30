import pytest

from local_home_app.common.runtime_errors import TelegramIntegrationError
from local_home_app.ingestion.telegram_receipt_ingest import (
    TelegramReceiptCandidate,
    normalize_telegram_receipt_candidate,
)


def test_normalize_photo_receipt_candidate() -> None:
    candidate = normalize_telegram_receipt_candidate(
        {
            "chat_id": "5143357049",
            "message_id": "477",
            "user_id": "5143357049",
            "media_type": "photo",
            "file_id": "abc123",
            "file_unique_id": "unique123",
            "file_name": None,
            "mime_type": "image/jpeg",
            "file_size_bytes": 1024,
        }
    )

    assert isinstance(candidate, TelegramReceiptCandidate)
    assert candidate.media_type == "photo"
    assert candidate.file_id == "abc123"


def test_normalize_unsupported_media_type_raises() -> None:
    with pytest.raises(TelegramIntegrationError):
        normalize_telegram_receipt_candidate(
            {
                "chat_id": "5143357049",
                "message_id": "477",
                "user_id": "5143357049",
                "media_type": "video",
                "file_id": "abc123",
            }
        )
