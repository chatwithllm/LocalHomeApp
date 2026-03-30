# Module: live_runtime_integration.py

## Purpose
Connect Telegram updates to receipt extraction, runtime intake processing, and routing-ready outputs.

## Inputs
Telegram update payloads, filesystem path helper, intake store, Telegram bot client.

## Outputs
Routing-ready output messages or `None` when the update does not contain a supported receipt candidate.

## Dependencies
- telegram_update_handler
- runtime_intake_service
- routing_outputs

## Execution Context
Used by future live polling/update loop implementation.

## Required Permissions
Network access to Telegram Bot API and read/write access to local sensitive storage root.

## Expected Errors / Failure Modes
- malformed Telegram updates
- Telegram download failures
- local write failures

## Related Tests
- tests/unit/test_live_runtime_integration.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
