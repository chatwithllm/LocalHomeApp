"""Normalization runtime service for LocalHomeApp.

Purpose:
- Orchestrate merchant normalization, item cleanup, item normalization, and quality scoring.

Inputs:
- raw merchant name
- raw item name
- line total

Outputs:
- normalized merchant/item values and quality label

Dependencies:
- dataclasses
- merchant_normalizer
- line_item_cleaner
- item_normalizer
- quality_scoring

Execution context:
- used between parsing/storage/signal layers.

Required permissions:
- none directly.

Expected errors/failure modes:
- unknown inputs remain only lightly normalized

Related tests:
- tests/unit/test_normalization_runtime_service.py

Related docs:
- docs/modules/normalization-runtime-service.md
- docs/phases/data-quality-and-normalization.md
"""

from __future__ import annotations

from dataclasses import dataclass

from local_home_app.quality.item_normalizer import normalize_item_name
from local_home_app.quality.line_item_cleaner import clean_line_item_name
from local_home_app.quality.merchant_normalizer import normalize_merchant_name
from local_home_app.quality.quality_scoring import score_item_quality


@dataclass(frozen=True)
class NormalizedRecord:
    merchant_name: str | None
    cleaned_item_name: str | None
    normalized_item_name: str | None
    quality_label: str


def normalize_record(*, merchant_name: str | None, item_name: str | None, line_total: float | None) -> NormalizedRecord:
    normalized_merchant = normalize_merchant_name(merchant_name)
    cleaned_item = clean_line_item_name(item_name)
    normalized_item = normalize_item_name(cleaned_item)
    quality = score_item_quality(
        merchant_name=normalized_merchant,
        item_name=normalized_item,
        line_total=line_total,
    )
    return NormalizedRecord(
        merchant_name=normalized_merchant,
        cleaned_item_name=cleaned_item,
        normalized_item_name=normalized_item,
        quality_label=quality,
    )
