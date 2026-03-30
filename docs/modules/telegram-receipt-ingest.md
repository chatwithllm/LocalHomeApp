# Module: telegram_receipt_ingest.py

## Purpose
Normalize Telegram receipt-related payloads into intake-ready records.

## Inputs
Telegram message/event payload data.

## Outputs
Normalized receipt candidate objects.

## Dependencies
- standard library dataclasses/typing
- runtime_errors

## Execution Context
Used by the local intake service before media download.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- unsupported media types
- missing required Telegram identifiers

## Related Tests
- tests/unit/test_telegram_receipt_ingest.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
- docs/architecture/data-flow.md
