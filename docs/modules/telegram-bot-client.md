# Module: telegram_bot_client.py

## Purpose
Provide a minimal Telegram Bot API boundary for retrieving receipt media file paths and bytes.

## Inputs
Telegram bot token and file identifiers.

## Outputs
Telegram file paths and downloaded media bytes.

## Dependencies
- json
- urllib

## Execution Context
Used during live receipt intake in Phase 1.

## Required Permissions
Network access to Telegram Bot API.

## Expected Errors / Failure Modes
- invalid bot token
- missing file path in Telegram response
- network failure
- unexpected payload format

## Related Tests
- tests/unit/test_telegram_bot_client.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
- docs/setup/telegram-bot-setup.md
