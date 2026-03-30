"""Telegram Bot API client helpers for LocalHomeApp.

Purpose:
- Provide a small Telegram download boundary for Phase 1 intake.

Inputs:
- Telegram bot token
- Telegram file identifiers

Outputs:
- Download URLs and downloaded media bytes

Dependencies:
- json
- urllib

Execution context:
- Used by the intake service during real Telegram media retrieval.

Required permissions:
- Network access to Telegram Bot API.

Expected errors/failure modes:
- invalid bot token
- missing file path
- network failure
- unexpected Telegram API payload

Related tests:
- tests/unit/test_telegram_bot_client.py

Related docs:
- docs/modules/telegram-bot-client.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

import json
from urllib.request import urlopen

from local_home_app.common.runtime_errors import TelegramIntegrationError


class TelegramBotClient:
    """Minimal Telegram Bot API client for receipt intake."""

    def __init__(self, bot_token: str) -> None:
        self.bot_token = bot_token

    def get_file_path(self, file_id: str) -> str:
        url = f"https://api.telegram.org/bot{self.bot_token}/getFile?file_id={file_id}"
        with urlopen(url) as response:  # noqa: S310
            payload = json.loads(response.read().decode("utf-8"))

        if not payload.get("ok"):
            raise TelegramIntegrationError(f"Telegram getFile failed for file_id={file_id}")

        result = payload.get("result") or {}
        file_path = result.get("file_path")
        if not file_path:
            raise TelegramIntegrationError("Telegram getFile response missing file_path")
        return str(file_path)

    def download_file_bytes(self, file_path: str) -> bytes:
        url = f"https://api.telegram.org/file/bot{self.bot_token}/{file_path}"
        with urlopen(url) as response:  # noqa: S310
            return response.read()
