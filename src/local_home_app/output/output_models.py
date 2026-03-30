"""Output models for LocalHomeApp.

Purpose:
- Represent structured output payloads for reports, summaries, and exports.

Inputs:
- parsed receipts, purchase history, and signal summaries.

Outputs:
- structured output records.

Dependencies:
- dataclasses
- typing

Execution context:
- used by report builders, formatters, and output runtime services.

Required permissions:
- none directly.

Expected errors/failure modes:
- missing required summary metadata.

Related tests:
- tests/unit/test_output_models.py

Related docs:
- docs/modules/output-models.md
- docs/phases/phase-06-output-integration.md
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class ReceiptSummaryOutput:
    merchant_name: Optional[str]
    receipt_date: Optional[str]
    total: Optional[float]
    parse_status: str


@dataclass(frozen=True)
class PurchaseHistorySummaryOutput:
    receipt_count: int
    merchants: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class SignalSummaryOutput:
    lines: List[str] = field(default_factory=list)
