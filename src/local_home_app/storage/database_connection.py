"""Database connection helpers for LocalHomeApp.

Purpose:
- Provide a central SQLite connection boundary for LocalHomeApp storage.

Inputs:
- database file path

Outputs:
- sqlite3 connection objects

Dependencies:
- sqlite3
- pathlib

Execution context:
- used by storage repositories and migration workflows.

Required permissions:
- read/write access to local database path

Expected errors/failure modes:
- invalid database path
- connection failure

Related tests:
- tests/unit/test_database_connection.py

Related docs:
- docs/modules/database-connection.md
- docs/phases/phase-04-local-storage.md
"""

from __future__ import annotations

import sqlite3
from pathlib import Path


def create_database_connection(database_path: Path) -> sqlite3.Connection:
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection
