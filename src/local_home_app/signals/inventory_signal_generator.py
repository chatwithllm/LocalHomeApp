"""Inventory signal generation for LocalHomeApp.

Purpose:
- Produce simple replenishment-style signals from purchase pattern observations.

Inputs:
- purchase pattern signals

Outputs:
- inventory signals

Dependencies:
- signal_models

Execution context:
- used by future recommendation workflows.

Required permissions:
- none directly.

Expected errors/failure modes:
- sparse pattern data leading to low-confidence signals

Related tests:
- tests/unit/test_inventory_signal_generator.py

Related docs:
- docs/modules/inventory-signal-generator.md
- docs/phases/phase-05-inventory-signals.md
"""

from __future__ import annotations

from typing import Iterable, List

from local_home_app.signals.signal_models import InventorySignal, PurchasePatternSignal


def generate_inventory_signals(pattern_signals: Iterable[PurchasePatternSignal]) -> List[InventorySignal]:
    signals = []
    for pattern in pattern_signals:
        if pattern.purchase_count >= 2 and pattern.average_days_between_purchases is not None:
            signals.append(
                InventorySignal(
                    item_name=pattern.item_name,
                    merchant_name=pattern.merchant_name,
                    signal_type='repeat_purchase_pattern',
                    reason=(
                        f"Observed {pattern.purchase_count} purchases; average interval "
                        f"{pattern.average_days_between_purchases:.1f} days"
                    ),
                    confidence_summary='low',
                )
            )
    return signals
