"""Intake result models for LocalHomeApp Phase 1.

Purpose:
- Represent the output of runtime intake flows, including operational messages.

Inputs:
- intake records and formatted operational messages

Outputs:
- structured runtime result objects

Dependencies:
- dataclasses
- intake_event_store

Execution context:
- used by runtime intake flows

Required permissions:
- none directly

Expected errors/failure modes:
- n/a

Related tests:
- tests/unit/test_runtime_intake_service.py

Related docs:
- docs/modules/intake-result.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from local_home_app.ingestion.intake_event_store import IntakeEventRecord


@dataclass(frozen=True)
class RuntimeIntakeResult:
    record: Optional[IntakeEventRecord]
    worker_message: Optional[str]
    alert_message: Optional[str]
    stored_file_path: Optional[Path]
