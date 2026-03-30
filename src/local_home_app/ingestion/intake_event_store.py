"""Intake event metadata model for LocalHomeApp.

Purpose:
- Represent intake event metadata for receipt artifacts.

Inputs:
- Intake candidate data and local storage details.

Outputs:
- Intake event metadata records for persistence.

Dependencies:
- dataclasses

Execution context:
- Used after media download planning and during intake persistence.

Required permissions:
- None directly; persistence layer will require local storage/database access.

Expected errors/failure modes:
- Missing required provenance fields.

Related tests:
- tests/unit/test_intake_event_store.py

Related docs:
- docs/modules/intake-event-store.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class IntakeEventRecord:
    """Metadata for a locally stored intake event."""

    intake_id: str
    source_channel: str
    source_account_id: str
    telegram_chat_id: str
    telegram_message_id: str
    telegram_user_id: str
    telegram_file_id: str
    telegram_file_unique_id: Optional[str]
    stored_at_path: str
    media_type: str
    mime_type: Optional[str]
    file_size_bytes: Optional[int]
    sha256: Optional[str]
    intake_status: str
    duplicate_of_intake_id: Optional[str] = None
    notes: Optional[str] = None
