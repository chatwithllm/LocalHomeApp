# Module: storage_schema.py

## Purpose
Define the initial SQLite schema for LocalHomeApp storage.

## Inputs
SQLite connection.

## Outputs
Created schema tables and indexes.

## Dependencies
- sqlite3

## Execution Context
Used by migration and setup workflows.

## Required Permissions
Write access to local database.

## Expected Errors / Failure Modes
- schema creation failure

## Related Tests
- tests/unit/test_storage_schema.py

## Related Docs
- docs/phases/phase-04-local-storage.md
