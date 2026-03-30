"""Database migration runner for LocalHomeApp.

Purpose:
- Apply the current storage schema to a local database connection.

Inputs:
- sqlite3 connection

Outputs:
- initialized schema state

Dependencies:
- storage_schema

Execution context:
- used during setup and local storage initialization.

Required permissions:
- write access to local database

Expected errors/failure modes:
- schema creation failure

Related tests:
- tests/unit/test_database_migration_runner.py

Related docs:
- docs/modules/database-migration-runner.md
- docs/phases/phase-04-local-storage.md
"""

from __future__ import annotations

import sqlite3

from local_home_app.storage.storage_schema import create_storage_schema


def run_migrations(connection: sqlite3.Connection) -> None:
    create_storage_schema(connection)
