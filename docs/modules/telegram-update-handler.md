# Module: telegram_update_handler.py

## Purpose
Extract receipt candidates from raw Telegram update payloads.

## Inputs
Telegram update payloads.

## Outputs
Normalized receipt candidates or `None` for unsupported updates.

## Dependencies
- telegram_receipt_ingest

## Execution Context
Used by the live runtime intake integration layer.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- malformed Telegram updates
- unsupported message structures

## Related Tests
- tests/unit/test_telegram_update_handler.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
