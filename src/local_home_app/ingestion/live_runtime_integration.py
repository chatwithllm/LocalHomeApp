"""Live runtime integration helpers for LocalHomeApp Phase 1.

Purpose:
- Connect Telegram updates to receipt extraction, runtime intake processing, and routing-ready outputs.

Inputs:
- Telegram update payload
- filesystem path helper
- intake store
- Telegram bot client

Outputs:
- routing-ready output messages or None when the update is not a receipt intake candidate

Dependencies:
- telegram_update_handler
- runtime_intake_service
- routing_outputs

Execution context:
- Used by future live polling/update loop implementation.

Required permissions:
- Network access to Telegram Bot API
- read/write access to local sensitive storage root

Expected errors/failure modes:
- malformed updates
- Telegram download failures
- local write failures

Related tests:
- tests/unit/test_live_runtime_integration.py

Related docs:
- docs/modules/live-runtime-integration.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from typing import Any, Optional

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.ingestion.live_runtime_integration import __name__ as _self_name  # noqa: F401
from local_home_app.ingestion.local_intake_store import LocalIntakeStore
from local_home_app.ingestion.routing_outputs import IntakeRoutingOutputs, build_routing_outputs
from local_home_app.ingestion.runtime_intake_service import process_telegram_candidate_via_bot
from local_home_app.ingestion.telegram_bot_client import TelegramBotClient
from local_home_app.ingestion.telegram_update_handler import extract_receipt_candidate_from_update


def handle_telegram_update_for_intake(
    *,
    update: dict[str, Any],
    paths: FileSystemPaths,
    store: LocalIntakeStore,
    bot_client: TelegramBotClient,
) -> Optional[IntakeRoutingOutputs]:
    """Handle a Telegram update for receipt intake if it contains supported media."""

    candidate = extract_receipt_candidate_from_update(update)
    if candidate is None:
        return None

    result = process_telegram_candidate_via_bot(
        candidate=candidate,
        paths=paths,
        store=store,
        bot_client=bot_client,
    )
    return build_routing_outputs(result)
