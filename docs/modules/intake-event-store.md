# Module: intake_event_store.py

## Purpose
Define the intake metadata record model for receipt intake events.

## Inputs
Normalized intake candidate data and storage details.

## Outputs
Structured intake event metadata records.

## Dependencies
- dataclasses

## Execution Context
Used during and after media download planning.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- missing required provenance fields

## Related Tests
- tests/unit/test_intake_event_store.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
