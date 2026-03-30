"""Routing-ready output helpers for LocalHomeApp intake.

Purpose:
- Convert runtime intake results into channel-specific output payloads.

Inputs:
- runtime intake result

Outputs:
- main, worker, and alert output messages

Dependencies:
- dataclasses
- intake_result

Execution context:
- Used after runtime intake processing before surface-specific message delivery.

Required permissions:
- none directly

Expected errors/failure modes:
- incomplete runtime result data

Related tests:
- tests/unit/test_routing_outputs.py

Related docs:
- docs/modules/routing-outputs.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from local_home_app.ingestion.intake_result import RuntimeIntakeResult


@dataclass(frozen=True)
class IntakeRoutingOutputs:
    main_message: Optional[str]
    worker_message: Optional[str]
    alert_message: Optional[str]


def build_routing_outputs(result: RuntimeIntakeResult) -> IntakeRoutingOutputs:
    main_message: Optional[str] = None
    if result.record is not None:
        main_message = (
            f"Receipt received: intake_id={result.record.intake_id} "
            f"status={result.record.intake_status}"
        )

    return IntakeRoutingOutputs(
        main_message=main_message,
        worker_message=result.worker_message,
        alert_message=result.alert_message,
    )
