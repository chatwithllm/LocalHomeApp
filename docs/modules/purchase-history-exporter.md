# Module: purchase_history_exporter.py

## Purpose
Export purchase history rows in structured JSON form.

## Inputs
Purchase history rows.

## Outputs
JSON export text.

## Dependencies
- json

## Execution Context
Used for local export and future output workflows.

## Required Permissions
Write permission only when a caller persists the returned export text.

## Expected Errors / Failure Modes
- non-serializable row content

## Related Tests
- tests/unit/test_purchase_history_exporter.py

## Related Docs
- docs/phases/phase-06-output-integration.md
