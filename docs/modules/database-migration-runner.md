# Module: database_migration_runner.py

## Purpose
Apply the current storage schema to a local database connection.

## Inputs
SQLite connection.

## Outputs
Initialized schema state.

## Dependencies
- storage_schema

## Execution Context
Used during setup and local storage initialization.

## Required Permissions
Write access to local database.

## Expected Errors / Failure Modes
- schema creation failure

## Related Tests
- tests/unit/test_database_migration_runner.py

## Related Docs
- docs/phases/phase-04-local-storage.md
