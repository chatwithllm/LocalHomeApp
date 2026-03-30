"""Telegram update handling for LocalHomeApp Phase 1.

Purpose:
- Extract receipt candidates from raw Telegram update payloads.

Inputs:
- Telegram update payloads.

Outputs:
- normalized receipt candidates or None when the update is not a supported receipt message.

Dependencies:
- telegram_receipt_ingest

Execution context:
- Used by the live runtime intake integration layer.

Required permissions:
- None directly.

Expected errors/failure modes:
- malformed Telegram update payloads
- unsupported message structures

Related tests:
- tests/unit/test_telegram_update_handler.py

Related docs:
- docs/modules/telegram-update-handler.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from typing import Any, Optional

from local_home_app.ingestion.telegram_receipt_ingest import (
    TelegramReceiptCandidate,
    normalize_telegram_receipt_candidate,
)


def extract_receipt_candidate_from_update(
    update: dict[str, Any],
) -> Optional[TelegramReceiptCandidate]:
    """Extract a normalized receipt candidate from a Telegram update payload."""

    message = update.get("message")
    if not isinstance(message, dict):
        return None

    base_payload = {
        "chat_id": str(message["chat"]["id"]),
        "message_id": str(message["message_id"]),
        "user_id": str(message["from"]["id"]),
    }

    if message.get("photo"):
        photo = message["photo"][-1]
        return normalize_telegram_receipt_candidate(
            {
                **base_payload,
                "media_type": "photo",
                "file_id": photo["file_id"],
                "file_unique_id": photo.get("file_unique_id"),
                "file_name": None,
                "mime_type": "image/jpeg",
                "file_size_bytes": photo.get("file_size"),
            }
        )

    if message.get("document"):
        document = message["document"]
        return normalize_telegram_receipt_candidate(
            {
                **base_payload,
                "media_type": "document",
                "file_id": document["file_id"],
                "file_unique_id": document.get("file_unique_id"),
                "file_name": document.get("file_name"),
                "mime_type": document.get("mime_type"),
                "file_size_bytes": document.get("file_size"),
            }
        )

    return None
