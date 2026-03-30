# Module: telegram_media_download.py

## Purpose
Plan local artifact storage paths for Telegram receipt media.

## Inputs
Normalized Telegram receipt candidate and filesystem path helpers.

## Outputs
Target local storage path for receipt artifacts.

## Dependencies
- pathlib
- telegram_receipt_ingest
- file_system_paths

## Execution Context
Used during receipt intake before and during media download.

## Required Permissions
Write access to local sensitive storage root.

## Expected Errors / Failure Modes
- unsupported or unknown file extension
- directory creation failures

## Related Tests
- tests/unit/test_telegram_media_download.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
- docs/architecture/privacy-boundaries.md
