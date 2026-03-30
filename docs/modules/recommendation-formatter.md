# Module: recommendation_formatter.py

## Purpose
Convert signal records into compact user-facing recommendation text.

## Inputs
Inventory signals and price expectation signals.

## Outputs
Formatted recommendation lines.

## Dependencies
- signal_models

## Execution Context
Used by future user-facing reporting/output workflows.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- incomplete signal data

## Related Tests
- tests/unit/test_recommendation_formatter.py

## Related Docs
- docs/phases/phase-05-inventory-signals.md
