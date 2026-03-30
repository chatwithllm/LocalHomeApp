"""Runtime intake service flow for LocalHomeApp Phase 1.

Purpose:
- Connect normalized Telegram receipt candidates to validation, real Telegram file retrieval, local intake orchestration, and operational messaging.

Inputs:
- Telegram receipt candidate
- filesystem path helper
- intake store
- Telegram bot client

Outputs:
- structured runtime intake result

Dependencies:
- telegram_bot_client
- intake_orchestrator
- receipt_validation
- intake_events
- intake_result

Execution context:
- Used by the local intake service entry point.

Required permissions:
- Network access to Telegram Bot API
- Read/write access to local sensitive storage root

Expected errors/failure modes:
- download failure
- invalid Telegram file metadata
- local write failure

Related tests:
- tests/unit/test_runtime_intake_service.py

Related docs:
- docs/modules/runtime-intake-service.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.common.runtime_errors import TelegramIntegrationError
from local_home_app.ingestion.intake_events import (
    format_alert_validation_message,
    format_worker_intake_message,
)
from local_home_app.ingestion.intake_orchestrator import process_local_receipt_intake
from local_home_app.ingestion.intake_result import RuntimeIntakeResult
from local_home_app.ingestion.intake_status import FAILED_DOWNLOAD, REJECTED
from local_home_app.ingestion.local_intake_store import LocalIntakeStore
from local_home_app.ingestion.receipt_validation import validate_receipt_candidate
from local_home_app.ingestion.telegram_bot_client import TelegramBotClient
from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


def process_telegram_candidate_via_bot(
    *,
    candidate: TelegramReceiptCandidate,
    paths: FileSystemPaths,
    store: LocalIntakeStore,
    bot_client: TelegramBotClient,
) -> RuntimeIntakeResult:
    """Validate, download, and process a Telegram receipt candidate."""

    validation = validate_receipt_candidate(candidate)
    if not validation.accepted:
        return RuntimeIntakeResult(
            record=None,
            worker_message=None,
            alert_message=format_alert_validation_message(
                candidate_chat_id=candidate.chat_id,
                candidate_message_id=candidate.message_id,
                validation=validation,
            ),
            stored_file_path=None,
        )

    try:
        file_path = bot_client.get_file_path(candidate.file_id)
        file_bytes = bot_client.download_file_bytes(file_path)
    except TelegramIntegrationError as exc:
        return RuntimeIntakeResult(
            record=None,
            worker_message=None,
            alert_message=(
                f"Receipt intake {FAILED_DOWNLOAD}: chat={candidate.chat_id} "
                f"message={candidate.message_id} reason={exc}"
            ),
            stored_file_path=None,
        )

    orchestration_result = process_local_receipt_intake(
        candidate=candidate,
        file_bytes=file_bytes,
        paths=paths,
        store=store,
    )

    return RuntimeIntakeResult(
        record=orchestration_result.record,
        worker_message=format_worker_intake_message(orchestration_result.record),
        alert_message=None,
        stored_file_path=orchestration_result.stored_file_path,
    )
