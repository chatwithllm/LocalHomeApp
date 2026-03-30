"""Telegram receipt intake normalization for LocalHomeApp.

Purpose:
- Normalize Telegram receipt-related payloads into intake-ready records.

Inputs:
- Telegram event/message payload data.

Outputs:
- Intake candidate models describing receipt media to download.

Dependencies:
- standard library dataclasses/typing

Execution context:
- Used by the local intake service before media download.

Required permissions:
- None directly; operates on inbound payload data.

Expected errors/failure modes:
- Unsupported payload type.
- Missing required Telegram media identifiers.

Related tests:
- tests/unit/test_telegram_receipt_ingest.py

Related docs:
- docs/modules/telegram-receipt-ingest.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from local_home_app.common.runtime_errors import TelegramIntegrationError


SUPPORTED_MEDIA_TYPES = {"photo", "document"}


@dataclass(frozen=True)
class TelegramReceiptCandidate:
    """Normalized Telegram receipt candidate for local intake."""

    chat_id: str
    message_id: str
    user_id: str
    media_type: str
    file_id: str
    file_unique_id: Optional[str]
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size_bytes: Optional[int]


def normalize_telegram_receipt_candidate(message: dict[str, Any]) -> TelegramReceiptCandidate:
    """Normalize a Telegram message payload into a receipt candidate."""

    chat_id = str(message["chat_id"])
    message_id = str(message["message_id"])
    user_id = str(message["user_id"])
    media_type = message["media_type"]

    if media_type not in SUPPORTED_MEDIA_TYPES:
        raise TelegramIntegrationError(f"Unsupported Telegram media type: {media_type}")

    return TelegramReceiptCandidate(
        chat_id=chat_id,
        message_id=message_id,
        user_id=user_id,
        media_type=media_type,
        file_id=str(message["file_id"]),
        file_unique_id=(
            str(message["file_unique_id"]) if message.get("file_unique_id") is not None else None
        ),
        file_name=message.get("file_name"),
        mime_type=message.get("mime_type"),
        file_size_bytes=message.get("file_size_bytes"),
    )
