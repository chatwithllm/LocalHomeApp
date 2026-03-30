"""Receipt deduplication helpers for LocalHomeApp.

Purpose:
- Provide explicit duplicate-detection helpers for receipt intake.

Inputs:
- Telegram file identity values.
- Content hashes.
- Existing intake event metadata.

Outputs:
- Duplicate match decisions.

Dependencies:
- intake_event_store

Execution context:
- Used during receipt intake before downstream processing.

Required permissions:
- None directly.

Expected errors/failure modes:
- Ambiguous partial metadata in comparison paths.

Related tests:
- tests/unit/test_receipt_deduplication.py

Related docs:
- docs/modules/receipt-deduplication.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from typing import Iterable, Optional

from local_home_app.ingestion.intake_event_store import IntakeEventRecord


def find_duplicate_intake_event(
    *,
    telegram_file_unique_id: Optional[str],
    sha256: Optional[str],
    existing_records: Iterable[IntakeEventRecord],
) -> Optional[IntakeEventRecord]:
    """Return the first matching duplicate intake event if one exists."""

    for record in existing_records:
        if telegram_file_unique_id and record.telegram_file_unique_id == telegram_file_unique_id:
            return record
        if sha256 and record.sha256 == sha256:
            return record
    return None
