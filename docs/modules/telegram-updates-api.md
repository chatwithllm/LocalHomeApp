# Module: telegram_updates_api.py

## Purpose
Provide a minimal polling boundary for Telegram updates.

## Inputs
Bot token, optional offset, optional timeout.

## Outputs
Raw Telegram update payloads.

## Dependencies
- json
- urllib

## Execution Context
Used by the polling/update-consumption loop skeleton.

## Required Permissions
Network access to Telegram Bot API.

## Expected Errors / Failure Modes
- invalid bot token
- network failure
- unexpected Telegram response payload

## Related Tests
- tests/unit/test_telegram_updates_api.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
