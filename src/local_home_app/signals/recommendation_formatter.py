"""Recommendation formatting for LocalHomeApp.

Purpose:
- Convert signal records into compact user-facing recommendation text.

Inputs:
- inventory signals
- price expectation signals

Outputs:
- formatted recommendation lines

Dependencies:
- signal_models

Execution context:
- used by future user-facing reporting/output workflows.

Required permissions:
- none directly.

Expected errors/failure modes:
- incomplete signal data

Related tests:
- tests/unit/test_recommendation_formatter.py

Related docs:
- docs/modules/recommendation-formatter.md
- docs/phases/phase-05-inventory-signals.md
"""

from __future__ import annotations

from typing import Iterable, List

from local_home_app.signals.signal_models import InventorySignal, PriceExpectationSignal


def format_recommendations(
    inventory_signals: Iterable[InventorySignal],
    price_signals: Iterable[PriceExpectationSignal],
) -> List[str]:
    lines: List[str] = []
    for signal in inventory_signals:
        lines.append(f"{signal.item_name}: {signal.reason}")
    for signal in price_signals:
        if signal.average_price is not None:
            lines.append(
                f"{signal.item_name}: avg ${signal.average_price:.2f}, latest ${signal.latest_price:.2f}"
            )
    return lines
