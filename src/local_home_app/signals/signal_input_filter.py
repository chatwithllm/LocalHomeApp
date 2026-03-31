"""Signal input filtering for LocalHomeApp.

Purpose:
- Filter noisy purchase-history rows before signal generation and explain what was skipped.

Inputs:
- purchase history rows

Outputs:
- usable rows and skip-reason counts

Dependencies:
- collections
- typing

Execution context:
- used before pattern and price signal generation.

Required permissions:
- none directly.

Expected errors/failure modes:
- malformed row shapes

Related tests:
- tests/unit/test_signal_input_filter.py

Related docs:
- docs/modules/signal-input-filter.md
- docs/phases/phase-05-inventory-signals.md
"""

from __future__ import annotations

from collections import Counter
from typing import Iterable, List, Tuple

from local_home_app.quality.normalization_runtime_service import normalize_record


NOISY_ITEM_HINTS = [
    'savings',
    'balance',
    'feedback',
    'jobs',
    'fuel points',
    'receipt',
    'visa',
    'mastercard',
    'customer',
    'sales id',
]


def filter_signal_input_rows(rows: Iterable[dict]) -> Tuple[List[dict], Counter]:
    usable: List[dict] = []
    skipped = Counter()

    for row in rows:
        merchant_name = row.get('merchant_name')
        item_name = row.get('item_name')
        line_total = row.get('line_total')

        normalized_record = normalize_record(
            merchant_name=merchant_name,
            item_name=item_name,
            line_total=line_total,
        )
        normalized_item_name = normalized_record.normalized_item_name

        if not item_name:
            skipped['missing_item_name'] += 1
            continue
        if not normalized_item_name:
            skipped['empty_after_normalization'] += 1
            continue

        normalized = normalized_item_name.strip().lower()
        if len(normalized) < 4:
            skipped['too_short'] += 1
            continue
        if any(hint in normalized for hint in NOISY_ITEM_HINTS):
            skipped['noisy_item_name'] += 1
            continue
        if line_total is None:
            skipped['missing_price'] += 1
            continue
        if normalized_record.quality_label == 'weak':
            skipped['weak_quality'] += 1
            continue

        usable.append(
            {
                **row,
                'merchant_name': normalized_record.merchant_name,
                'item_name': normalized_item_name,
                'quality_label': normalized_record.quality_label,
            }
        )

    return usable, skipped
