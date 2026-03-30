"""Price expectation analysis for LocalHomeApp.

Purpose:
- Derive basic observed price expectations from purchase history.

Inputs:
- purchase history rows

Outputs:
- price expectation signals

Dependencies:
- collections
- signal_models

Execution context:
- used by inventory and recommendation workflows.

Required permissions:
- none directly.

Expected errors/failure modes:
- sparse or malformed price values

Related tests:
- tests/unit/test_price_expectation_engine.py

Related docs:
- docs/modules/price-expectation-engine.md
- docs/phases/phase-05-inventory-signals.md
"""

from __future__ import annotations

from collections import defaultdict
from typing import Iterable, List

from local_home_app.signals.signal_models import PriceExpectationSignal


def build_price_expectations(rows: Iterable[dict]) -> List[PriceExpectationSignal]:
    grouped = defaultdict(list)
    for row in rows:
        price = row.get('line_total')
        if price is None:
            continue
        grouped[(row.get('merchant_name'), row.get('item_name'))].append(price)

    signals = []
    for (merchant_name, item_name), prices in grouped.items():
        signals.append(
            PriceExpectationSignal(
                item_name=item_name,
                merchant_name=merchant_name,
                average_price=sum(prices) / len(prices),
                min_price=min(prices),
                max_price=max(prices),
                latest_price=prices[-1],
            )
        )
    return signals
