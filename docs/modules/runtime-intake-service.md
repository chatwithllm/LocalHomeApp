# Module: runtime_intake_service.py

## Purpose
Connect Telegram receipt candidates to validation, Telegram file retrieval, local receipt intake orchestration, and operational messaging.

## Inputs
Telegram receipt candidate, filesystem path helper, intake store, Telegram bot client.

## Outputs
Structured runtime intake result.

## Dependencies
- telegram_bot_client
- intake_orchestrator
- receipt_validation
- intake_events
- intake_result

## Execution Context
Used by the local intake service entry point.

## Required Permissions
Network access to Telegram Bot API and read/write access to local sensitive storage root.

## Expected Errors / Failure Modes
- Telegram download failure
- invalid Telegram file metadata
- rejected payload validation
- local write or persistence failure

## Related Tests
- tests/unit/test_runtime_intake_service.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
