"""Worker and alert event formatting for LocalHomeApp intake.

Purpose:
- Format operational messages for Workers and Alerts surfaces.

Inputs:
- intake records and validation results

Outputs:
- formatted text messages for operational channels

Dependencies:
- intake_event_store
- receipt_validation

Execution context:
- used by runtime intake flows when reporting progress or failures

Required permissions:
- none directly

Expected errors/failure modes:
- incomplete intake data for formatting

Related tests:
- tests/unit/test_intake_events.py

Related docs:
- docs/modules/intake-events.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from local_home_app.ingestion.intake_event_store import IntakeEventRecord
from local_home_app.ingestion.receipt_validation import ReceiptValidationResult


def format_worker_intake_message(record: IntakeEventRecord) -> str:
    return (
        f"Receipt intake {record.intake_status}: intake_id={record.intake_id} "
        f"chat={record.telegram_chat_id} message={record.telegram_message_id} "
        f"path={record.stored_at_path}"
    )


def format_alert_validation_message(
    *, candidate_chat_id: str,
    candidate_message_id: str,
    validation: ReceiptValidationResult,
) -> str:
    return (
        f"Receipt intake validation failed: chat={candidate_chat_id} "
        f"message={candidate_message_id} reason={validation.reason}"
    )
