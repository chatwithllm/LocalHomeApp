#!/usr/bin/env python3
"""Query LocalHomeApp purchase history through the interaction service.

Purpose:
- Provide a local, user-oriented query entry point for recent receipts and item history.

Inputs:
- optional merchant filter
- optional item query
- limit

Outputs:
- concise text summary for terminal or future messaging use

Dependencies:
- argparse
- pathlib
- sys
- interaction_service
- database_connection
- purchase_history_repository

Execution context:
- run manually on the local machine.

Required permissions:
- read access to the local LocalHomeApp database.

Expected errors/failure modes:
- missing or empty database
- sparse results for the requested query

Related docs:
- docs/modules/interaction-service.md
- docs/phases/phase-10-user-interaction-layer.md
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.query.interaction_service import InteractionService
from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.purchase_history_repository import PurchaseHistoryRepository


def main() -> int:
    parser = argparse.ArgumentParser(description="Query LocalHomeApp purchase history")
    parser.add_argument('--merchant', help='Filter recent receipts by merchant')
    parser.add_argument('--item', help='Search purchase history by item text')
    parser.add_argument('--limit', type=int, default=5, help='Maximum rows to show')
    args = parser.parse_args()

    database_path = Path('/Users/assistant/LocalHomeAppSensitiveData/database/local_home_app.sqlite')
    connection = create_database_connection(database_path)
    try:
        service = InteractionService(PurchaseHistoryRepository(connection))
        if args.item:
            summary = service.summarize_item_history(args.item, limit=args.limit)
        elif args.merchant:
            summary = service.summarize_receipts_for_merchant(args.merchant, limit=args.limit)
        else:
            summary = service.summarize_recent_receipts(limit=args.limit)

        print(summary.title)
        if summary.lines:
            for line in summary.lines:
                print(f'- {line}')
        else:
            print('- No matching history found')
    finally:
        connection.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
