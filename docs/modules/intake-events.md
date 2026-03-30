# Module: intake_events.py

## Purpose
Format operational worker and alert messages for receipt intake events.

## Inputs
Intake event records and validation results.

## Outputs
Formatted operational messages.

## Dependencies
- intake_event_store
- receipt_validation

## Execution Context
Used by runtime intake flows.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- incomplete intake data for formatting

## Related Tests
- tests/unit/test_intake_events.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
