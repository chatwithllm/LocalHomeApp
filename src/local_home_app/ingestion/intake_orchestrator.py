"""Phase 1 local intake orchestration for LocalHomeApp.

Purpose:
- Orchestrate local receipt intake steps around storage planning, hashing, duplicate checks, and metadata persistence.

Inputs:
- Telegram receipt candidate
- file bytes
- filesystem path helper
- local intake store

Outputs:
- Intake event metadata record
- duplicate match information when applicable

Dependencies:
- telegram_media_download
- file_hashing
- intake_workflow
- receipt_deduplication
- local_intake_store

Execution context:
- Used by the local intake service after message normalization.

Required permissions:
- Read/write access to local sensitive storage root.

Expected errors/failure modes:
- file write failure
- hashing failure
- metadata persistence failure

Related tests:
- tests/unit/test_intake_orchestrator.py

Related docs:
- docs/modules/intake-orchestrator.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.ingestion.file_hashing import compute_sha256
from local_home_app.ingestion.intake_event_store import IntakeEventRecord
from local_home_app.ingestion.intake_workflow import build_intake_event_record
from local_home_app.ingestion.local_intake_store import LocalIntakeStore
from local_home_app.ingestion.receipt_deduplication import find_duplicate_intake_event
from local_home_app.ingestion.telegram_media_download import build_local_receipt_artifact_path
from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


@dataclass(frozen=True)
class IntakeOrchestrationResult:
    record: IntakeEventRecord
    duplicate_of: Optional[IntakeEventRecord]
    stored_file_path: Path


def process_local_receipt_intake(
    *,
    candidate: TelegramReceiptCandidate,
    file_bytes: bytes,
    paths: FileSystemPaths,
    store: LocalIntakeStore,
) -> IntakeOrchestrationResult:
    """Execute the local Phase 1 intake workflow for a receipt artifact."""

    target_path = build_local_receipt_artifact_path(candidate, paths)
    target_path.write_bytes(file_bytes)
    sha256 = compute_sha256(target_path)

    existing_records = store.load_all()
    duplicate = find_duplicate_intake_event(
        telegram_file_unique_id=candidate.file_unique_id,
        sha256=sha256,
        existing_records=existing_records,
    )

    record = build_intake_event_record(
        candidate=candidate,
        stored_at_path=target_path,
        sha256=sha256,
    )

    if duplicate is not None:
        record = IntakeEventRecord(
            **{
                **record.__dict__,
                "intake_status": "duplicate",
                "duplicate_of_intake_id": duplicate.intake_id,
            }
        )

    store.append(record)

    return IntakeOrchestrationResult(
        record=record,
        duplicate_of=duplicate,
        stored_file_path=target_path,
    )
