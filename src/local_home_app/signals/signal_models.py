"""Signal models for LocalHomeApp.

Purpose:
- Represent structured purchase-history signals and recommendations.

Inputs:
- analyzed purchase history observations.

Outputs:
- structured signal records.

Dependencies:
- dataclasses
- typing

Execution context:
- used by signal analysis and recommendation formatting components.

Required permissions:
- none directly.

Expected errors/failure modes:
- missing required signal metadata.

Related tests:
- tests/unit/test_signal_models.py

Related docs:
- docs/modules/signal-models.md
- docs/phases/phase-05-inventory-signals.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PurchasePatternSignal:
    item_name: str
    merchant_name: Optional[str]
    purchase_count: int
    last_purchase_date: Optional[str]
    average_days_between_purchases: Optional[float]


@dataclass(frozen=True)
class PriceExpectationSignal:
    item_name: str
    merchant_name: Optional[str]
    average_price: Optional[float]
    min_price: Optional[float]
    max_price: Optional[float]
    latest_price: Optional[float]


@dataclass(frozen=True)
class InventorySignal:
    item_name: str
    merchant_name: Optional[str]
    signal_type: str
    reason: str
    confidence_summary: Optional[str]
