# Script: run_purchase_history_summary.py

## Purpose
Print a simple purchase history summary from the LocalHomeApp SQLite storage layer.

## Inputs
Current local SQLite database.

## Outputs
Summary rows with merchant, date, total, and line-item count.

## Dependencies
- database_connection
- purchase_history_repository

## Execution Context
Used for local storage validation and quick inspection.

## Required Permissions
Read access to the local database.

## Expected Errors / Failure Modes
- missing database
- missing schema
- query failures

## Related Tests
- tests/unit/test_purchase_history_summary.py

## Related Docs
- docs/phases/phase-04-local-storage.md
- docs/setup/database-operations.md
