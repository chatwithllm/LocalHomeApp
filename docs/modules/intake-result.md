# Module: intake_result.py

## Purpose
Represent structured runtime intake results, including operational worker and alert messages.

## Inputs
Intake records and formatted operational messages.

## Outputs
Structured runtime intake result objects.

## Dependencies
- dataclasses
- intake_event_store

## Execution Context
Used by runtime intake flows.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
n/a

## Related Tests
- tests/unit/test_runtime_intake_service.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
