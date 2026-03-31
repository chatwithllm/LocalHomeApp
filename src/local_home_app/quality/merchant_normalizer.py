"""Merchant normalization for LocalHomeApp.

Purpose:
- Normalize merchant name variants into a consistent canonical form.

Inputs:
- raw merchant name text

Outputs:
- canonical merchant name

Dependencies:
- none beyond standard library

Execution context:
- used after parsing and before downstream storage/signal use.

Required permissions:
- none directly.

Expected errors/failure modes:
- unknown merchant names remain unnormalized

Related tests:
- tests/unit/test_merchant_normalizer.py

Related docs:
- docs/modules/merchant-normalizer.md
- docs/phases/data-quality-and-normalization.md
"""

from __future__ import annotations


MERCHANT_RULES = {
    'kroger': 'Kroger',
    'walmart': 'Walmart',
    'wal*mart': 'Walmart',
    'micro center': 'Micro Center',
    'icro center': 'Micro Center',
    'meijer': 'Meijer',
    'metljer': 'Meijer',
    'sahara bazaar': 'Sahara Bazaar',
}


def normalize_merchant_name(raw_name: str | None) -> str | None:
    if raw_name is None:
        return None
    normalized = raw_name.strip().lower()
    for key, canonical in MERCHANT_RULES.items():
        if key in normalized:
            return canonical
    return raw_name.strip() or None
