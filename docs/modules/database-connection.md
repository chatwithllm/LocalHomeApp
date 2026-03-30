# Module: database_connection.py

## Purpose
Provide a central SQLite connection boundary for LocalHomeApp storage.

## Inputs
Database file path.

## Outputs
SQLite connection objects.

## Dependencies
- sqlite3
- pathlib

## Execution Context
Used by storage repositories and migration workflows.

## Required Permissions
Read/write access to local database path.

## Expected Errors / Failure Modes
- invalid database path
- connection failure

## Related Tests
- tests/unit/test_database_connection.py

## Related Docs
- docs/phases/phase-04-local-storage.md
