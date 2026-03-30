"""Minimal delivery hook abstractions for LocalHomeApp Phase 1.

Purpose:
- Represent where Main, Workers, and Alerts outputs would be delivered.

Inputs:
- routing-ready output messages

Outputs:
- delivery payload records for runtime use or later provider integration

Dependencies:
- dataclasses
- routing_outputs

Execution context:
- Used by the polling/update-consumption loop skeleton.

Required permissions:
- None directly.

Expected errors/failure modes:
- incomplete routing output data

Related tests:
- tests/unit/test_delivery_hooks.py

Related docs:
- docs/modules/delivery-hooks.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from local_home_app.ingestion.routing_outputs import IntakeRoutingOutputs


@dataclass(frozen=True)
class DeliveryPayload:
    target: str
    message: str


def build_delivery_payloads(outputs: IntakeRoutingOutputs) -> List[DeliveryPayload]:
    payloads: List[DeliveryPayload] = []
    if outputs.main_message:
        payloads.append(DeliveryPayload(target="main", message=outputs.main_message))
    if outputs.worker_message:
        payloads.append(DeliveryPayload(target="workers", message=outputs.worker_message))
    if outputs.alert_message:
        payloads.append(DeliveryPayload(target="alerts", message=outputs.alert_message))
    return payloads
