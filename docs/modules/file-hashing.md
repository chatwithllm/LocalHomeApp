# Module: file_hashing.py

## Purpose
Compute stable SHA-256 content hashes for locally stored receipt artifacts.

## Inputs
Local file paths.

## Outputs
SHA-256 hex digest strings.

## Dependencies
- hashlib
- pathlib

## Execution Context
Used after local receipt file download.

## Required Permissions
Read access to local receipt artifacts.

## Expected Errors / Failure Modes
- unreadable file
- missing file

## Related Tests
- tests/unit/test_file_hashing.py

## Related Docs
- docs/phases/phase-01-telegram-intake.md
