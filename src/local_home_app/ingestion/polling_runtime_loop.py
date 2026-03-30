"""Polling/update-consumption loop skeleton for LocalHomeApp Phase 1.

Purpose:
- Connect Telegram update polling to live runtime intake integration and delivery payload generation.

Inputs:
- Telegram updates API
- filesystem path helper
- intake store
- Telegram bot client

Outputs:
- processed update summaries and delivery payloads

Dependencies:
- telegram_updates_api
- live_runtime_integration
- delivery_hooks

Execution context:
- Used by the future intake runtime service.

Required permissions:
- Network access to Telegram Bot API
- read/write access to local sensitive storage root

Expected errors/failure modes:
- Telegram polling failure
- malformed update payloads
- local intake processing failure

Related tests:
- tests/unit/test_polling_runtime_loop.py

Related docs:
- docs/modules/polling-runtime-loop.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.ingestion.delivery_hooks import DeliveryPayload, build_delivery_payloads
from local_home_app.ingestion.live_runtime_integration import handle_telegram_update_for_intake
from local_home_app.ingestion.local_intake_store import LocalIntakeStore
from local_home_app.ingestion.telegram_bot_client import TelegramBotClient
from local_home_app.ingestion.telegram_updates_api import TelegramUpdatesApi


@dataclass(frozen=True)
class PollingLoopResult:
    next_offset: Optional[int]
    delivery_payloads: List[DeliveryPayload]


def process_polled_updates(
    *,
    updates_api: TelegramUpdatesApi,
    paths: FileSystemPaths,
    store: LocalIntakeStore,
    bot_client: TelegramBotClient,
    offset: Optional[int] = None,
    timeout: int = 0,
) -> PollingLoopResult:
    """Poll Telegram updates and convert receipt-related ones into delivery payloads."""

    updates = updates_api.get_updates(offset=offset, timeout=timeout)
    delivery_payloads: List[DeliveryPayload] = []
    next_offset = offset

    for update in updates:
        update_id = update.get("update_id")
        if isinstance(update_id, int):
            next_offset = update_id + 1

        outputs = handle_telegram_update_for_intake(
            update=update,
            paths=paths,
            store=store,
            bot_client=bot_client,
        )
        if outputs is None:
            continue

        delivery_payloads.extend(build_delivery_payloads(outputs))

    return PollingLoopResult(next_offset=next_offset, delivery_payloads=delivery_payloads)
