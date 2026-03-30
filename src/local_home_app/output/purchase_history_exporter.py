"""Purchase history exporting for LocalHomeApp.

Purpose:
- Export purchase history rows in structured JSON form.

Inputs:
- purchase history rows

Outputs:
- JSON export text

Dependencies:
- json

Execution context:
- used for local export and future output workflows.

Required permissions:
- write permission only when a caller persists the returned export text.

Expected errors/failure modes:
- non-serializable row content

Related tests:
- tests/unit/test_purchase_history_exporter.py

Related docs:
- docs/modules/purchase-history-exporter.md
- docs/phases/phase-06-output-integration.md
"""

from __future__ import annotations

import json
from typing import Iterable


def export_purchase_history_json(rows: Iterable[dict]) -> str:
    return json.dumps(list(rows), indent=2, sort_keys=True)
