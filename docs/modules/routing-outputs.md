# Module: routing_outputs.py

## Purpose
Convert runtime intake results into channel-ready messages for Main, Workers, and Alerts.

## Inputs
Runtime intake results.

## Outputs
Routing output messages for different Telegram surfaces.

## Dependencies
- intake_result
- dataclasses

## Execution Context
Used before surface-specific message delivery.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- incomplete runtime result data

## Related Tests
- tests/unit/test_routing_outputs.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
