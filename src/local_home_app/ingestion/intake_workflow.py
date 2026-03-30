"""Receipt intake workflow helpers for LocalHomeApp.

Purpose:
- Build intake metadata from normalized Telegram candidates and stored files.

Inputs:
- Telegram receipt candidate
- local artifact path
- content hash

Outputs:
- Intake event metadata record

Dependencies:
- uuid
- intake_event_store
- telegram_receipt_ingest

Execution context:
- Used after local download planning/execution during Phase 1 intake.

Required permissions:
- None directly.

Expected errors/failure modes:
- Missing required provenance values.
- Invalid storage path values.

Related tests:
- tests/unit/test_intake_workflow.py

Related docs:
- docs/modules/intake-workflow.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from local_home_app.ingestion.intake_event_store import IntakeEventRecord
from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


DEFAULT_SOURCE_ACCOUNT_ID = "default"
DEFAULT_INTAKE_STATUS = "received"


def build_intake_event_record(
    *,
    candidate: TelegramReceiptCandidate,
    stored_at_path: Path,
    sha256: str | None,
) -> IntakeEventRecord:
    """Build an intake event record from a normalized Telegram receipt candidate."""

    return IntakeEventRecord(
        intake_id=str(uuid4()),
        source_channel="telegram",
        source_account_id=DEFAULT_SOURCE_ACCOUNT_ID,
        telegram_chat_id=candidate.chat_id,
        telegram_message_id=candidate.message_id,
        telegram_user_id=candidate.user_id,
        telegram_file_id=candidate.file_id,
        telegram_file_unique_id=candidate.file_unique_id,
        stored_at_path=str(stored_at_path),
        media_type=candidate.media_type,
        mime_type=candidate.mime_type,
        file_size_bytes=candidate.file_size_bytes,
        sha256=sha256,
        intake_status=DEFAULT_INTAKE_STATUS,
    )
