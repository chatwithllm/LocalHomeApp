"""Item normalization scaffolding for LocalHomeApp.

Purpose:
- Provide a clear boundary for item-name normalization beyond basic cleanup.

Inputs:
- cleaned item name text

Outputs:
- normalized item identity text

Dependencies:
- none beyond standard library

Execution context:
- used before downstream signal generation and history aggregation.

Required permissions:
- none directly.

Expected errors/failure modes:
- unknown item variants remain near-original

Related tests:
- tests/unit/test_item_normalizer.py

Related docs:
- docs/modules/item-normalizer.md
- docs/phases/data-quality-and-normalization.md
"""

from __future__ import annotations


def normalize_item_name(cleaned_item_name: str | None) -> str | None:
    if cleaned_item_name is None:
        return None
    return cleaned_item_name.upper().strip() or None
