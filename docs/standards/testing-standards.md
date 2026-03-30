# Testing Standards

## Test categories
- unit tests
- integration tests
- regression tests
- fixture-based parsing/OCR tests

## Expectations by phase
- Phase 00: import/config/logging sanity
- Phase 01: Telegram intake mocks and artifact persistence
- Phase 02: OCR engine and preprocessing tests
- Phase 03: structured parsing regression tests
- Phase 04+: repository, migration, and signal-generation tests

## Core quality rule
Trust and correctness are more important than novelty. Low-confidence or ambiguous results should be flagged rather than silently accepted.
