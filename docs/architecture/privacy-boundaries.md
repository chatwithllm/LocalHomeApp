# Privacy Boundaries

## Local-only sensitive artifacts
The following artifacts must remain in local machine-controlled storage and must not be committed to GitHub:
- raw receipt images/documents
- OCR text outputs
- local SQLite databases
- exports containing household data
- secrets and tokens
- logs containing sensitive operational or household information
- manual review artifacts

## Recommended sensitive storage root
`/Users/assistant/LocalHomeAppSensitiveData`

## Suggested subdirectories
- `receipts/`
- `ocr_outputs/`
- `structured_outputs/`
- `database/`
- `exports/`
- `secrets/`
- `logs/`
- `manual_review/`

## Git boundary
GitHub is the source of truth for non-sensitive code and documentation only.

## Telegram boundary
Telegram is the intake and notification transport for V1. Sensitive raw receipt data should remain local after intake download and should not be redistributed casually across downstream channels.
