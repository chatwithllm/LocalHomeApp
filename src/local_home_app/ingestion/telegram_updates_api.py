"""Telegram update polling helpers for LocalHomeApp.

Purpose:
- Provide a minimal polling boundary for Telegram updates in Phase 1.

Inputs:
- bot token
- optional offset and timeout values

Outputs:
- raw Telegram update payloads

Dependencies:
- json
- urllib

Execution context:
- Used by the polling/update-consumption loop skeleton.

Required permissions:
- Network access to Telegram Bot API.

Expected errors/failure modes:
- invalid bot token
- network failure
- unexpected Telegram response payload

Related tests:
- tests/unit/test_telegram_updates_api.py

Related docs:
- docs/modules/telegram-updates-api.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

import json
from typing import Any, Optional
from urllib.parse import urlencode
from urllib.request import urlopen

from local_home_app.common.runtime_errors import TelegramIntegrationError


class TelegramUpdatesApi:
    """Minimal Telegram polling API helper."""

    def __init__(self, bot_token: str) -> None:
        self.bot_token = bot_token

    def get_updates(self, *, offset: Optional[int] = None, timeout: int = 0) -> list[dict[str, Any]]:
        params = {"timeout": timeout}
        if offset is not None:
            params["offset"] = offset

        query = urlencode(params)
        url = f"https://api.telegram.org/bot{self.bot_token}/getUpdates?{query}"
        with urlopen(url) as response:  # noqa: S310
            payload = json.loads(response.read().decode("utf-8"))

        if not payload.get("ok"):
            raise TelegramIntegrationError("Telegram getUpdates failed")

        result = payload.get("result")
        if not isinstance(result, list):
            raise TelegramIntegrationError("Telegram getUpdates returned invalid result payload")

        return result
