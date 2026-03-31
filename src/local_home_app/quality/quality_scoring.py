"""Quality scoring for LocalHomeApp structured data.

Purpose:
- Score parsed structured data for downstream usability.

Inputs:
- merchant name
- item name
- line total

Outputs:
- quality label

Dependencies:
- none beyond standard library

Execution context:
- used before signals and reports consume parsed data.

Required permissions:
- none directly.

Expected errors/failure modes:
- simplistic scoring during early iterations

Related tests:
- tests/unit/test_quality_scoring.py

Related docs:
- docs/modules/quality-scoring.md
- docs/phases/data-quality-and-normalization.md
"""

from __future__ import annotations


def score_item_quality(*, merchant_name: str | None, item_name: str | None, line_total: float | None) -> str:
    if merchant_name and item_name and line_total is not None:
        return 'usable'
    if item_name and line_total is not None:
        return 'partial'
    return 'weak'
