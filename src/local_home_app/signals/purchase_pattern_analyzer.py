"""Purchase pattern analysis for LocalHomeApp.

Purpose:
- Analyze item purchase history to derive repeat-purchase observations.

Inputs:
- purchase history rows

Outputs:
- purchase pattern signals

Dependencies:
- datetime
- collections
- signal_models

Execution context:
- used by inventory and price signal generation.

Required permissions:
- none directly.

Expected errors/failure modes:
- malformed date values
- sparse history for interval analysis

Related tests:
- tests/unit/test_purchase_pattern_analyzer.py

Related docs:
- docs/modules/purchase-pattern-analyzer.md
- docs/phases/phase-05-inventory-signals.md
"""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from typing import Iterable, List

from local_home_app.signals.signal_models import PurchasePatternSignal


def analyze_purchase_patterns(rows: Iterable[dict]) -> List[PurchasePatternSignal]:
    grouped = defaultdict(list)
    for row in rows:
        key = (row.get('merchant_name'), row.get('item_name'))
        grouped[key].append(row.get('receipt_date'))

    signals = []
    for (merchant_name, item_name), dates in grouped.items():
        parsed_dates = []
        for raw in dates:
            if raw:
                try:
                    parsed_dates.append(datetime.strptime(raw, '%m/%d/%y'))
                except ValueError:
                    continue
        parsed_dates.sort()

        avg_days = None
        if len(parsed_dates) >= 2:
            deltas = [
                (parsed_dates[i] - parsed_dates[i - 1]).days
                for i in range(1, len(parsed_dates))
            ]
            avg_days = sum(deltas) / len(deltas)

        signals.append(
            PurchasePatternSignal(
                item_name=item_name,
                merchant_name=merchant_name,
                purchase_count=len(dates),
                last_purchase_date=dates[-1] if dates else None,
                average_days_between_purchases=avg_days,
            )
        )
    return signals
