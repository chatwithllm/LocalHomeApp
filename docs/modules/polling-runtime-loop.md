# Module: polling_runtime_loop.py

## Purpose
Connect Telegram update polling to live receipt intake handling and delivery payload generation.

## Inputs
Telegram updates API, filesystem path helper, intake store, Telegram bot client.

## Outputs
Polling loop result with next offset and delivery payloads.

## Dependencies
- telegram_updates_api
- live_runtime_integration
- delivery_hooks

## Execution Context
Used by the future intake runtime service.

## Required Permissions
Network access to Telegram Bot API and read/write access to local sensitive storage root.

## Expected Errors / Failure Modes
- Telegram polling failure
- malformed updates
- local intake processing failure

## Related Tests
- tests/unit/test_polling_runtime_loop.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
