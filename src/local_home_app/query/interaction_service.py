"""User interaction/query service for LocalHomeApp.

Purpose:
- Provide simple query-oriented access to recent receipts and purchase history for user-facing responses.

Inputs:
- purchase history repository
- optional merchant/item filters

Outputs:
- concise structured summaries suitable for conversational delivery

Dependencies:
- dataclasses
- typing
- purchase_history_repository

Execution context:
- used by future messaging or local query scripts.

Required permissions:
- read access to local database through the repository layer.

Expected errors/failure modes:
- sparse or low-quality stored data yields partial answers

Related tests:
- tests/unit/test_interaction_service.py

Related docs:
- docs/modules/interaction-service.md
- docs/phases/phase-10-user-interaction-layer.md
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from local_home_app.storage.purchase_history_repository import PurchaseHistoryRepository


@dataclass(frozen=True)
class ReceiptInteractionRow:
    merchant_name: Optional[str]
    receipt_date: Optional[str]
    total: Optional[float]
    line_item_count: int


@dataclass(frozen=True)
class ItemInteractionRow:
    merchant_name: Optional[str]
    receipt_date: Optional[str]
    item_name: Optional[str]
    line_total: Optional[float]


@dataclass(frozen=True)
class InteractionSummary:
    title: str
    lines: List[str] = field(default_factory=list)


class InteractionService:
    def __init__(self, repository: PurchaseHistoryRepository) -> None:
        self.repository = repository

    def summarize_recent_receipts(self, limit: int = 5) -> InteractionSummary:
        rows = self.repository.summarize_recent_receipts(limit=limit)
        lines = [
            f"{row['receipt_date'] or 'Unknown date'} — {row['merchant_name'] or 'Unknown merchant'} — "
            f"total={row['total'] if row['total'] is not None else 'Unknown'} — items={row['line_item_count']}"
            for row in rows
        ]
        return InteractionSummary(title='Recent receipts', lines=lines)

    def summarize_receipts_for_merchant(self, merchant_name: str, limit: int = 5) -> InteractionSummary:
        rows = self.repository.summarize_recent_receipts(limit=limit, merchant_name=merchant_name)
        lines = [
            f"{row['receipt_date'] or 'Unknown date'} — total={row['total'] if row['total'] is not None else 'Unknown'} — items={row['line_item_count']}"
            for row in rows
        ]
        return InteractionSummary(title=f'Recent receipts for {merchant_name}', lines=lines)

    def summarize_item_history(self, item_query: str, limit: int = 10) -> InteractionSummary:
        rows = self.repository.list_line_items(limit=limit, item_query=item_query)
        lines = [
            f"{row['receipt_date'] or 'Unknown date'} — {row['merchant_name'] or 'Unknown merchant'} — "
            f"{row['item_name'] or 'Unknown item'} — {row['line_total'] if row['line_total'] is not None else 'Unknown'}"
            for row in rows
        ]
        return InteractionSummary(title=f'Item history for {item_query}', lines=lines)
