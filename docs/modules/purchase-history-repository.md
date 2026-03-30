# Module: purchase_history_repository.py

## Purpose
Provide query access to stored parsed receipt line items for household purchase history.

## Inputs
Query filters as needed later.

## Outputs
Purchase history rows.

## Dependencies
- sqlite3

## Execution Context
Used by later analytics, signal, and recommendation phases.

## Required Permissions
Read access to local database.

## Expected Errors / Failure Modes
- query failures

## Related Tests
- tests/unit/test_purchase_history_repository.py

## Related Docs
- docs/phases/phase-04-local-storage.md
