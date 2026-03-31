# Phase 09 — Real Receipt Evaluation and Signal Tightening

## Objective
Evaluate the OCR and downstream signal pipeline against real or realistic receipt artifacts, compare Apple Vision and Tesseract behavior, and tighten downstream filtering so weak/noisy inputs do less damage.

## Scope
- OCR engine comparison reporting
- practical OCR evaluation runner
- quality-aware signal input filtering
- downstream summary of skipped/weak inputs
- phase documentation and baseline tests

## Out of Scope
- cloud OCR
- advanced machine-learning ranking
- broad UI/dashboard work
- large parser rewrites

## Deliverables
- phase doc
- OCR evaluation summary model/helpers
- real-receipt evaluation script
- signal-filter tightening based on normalization/quality
- baseline tests and docs updates

## Risks
- synthetic fixtures may overstate success
- real receipt variation may reveal parser gaps beyond this phase
- over-filtering could suppress useful rows

## Dependencies
- completed OCR implementations
- parsing and normalization layers
- local test/runtime environment

## Acceptance Criteria
- OCR comparison results can be summarized in a practical, inspectable form
- Apple Vision and Tesseract can be evaluated through one local runner
- weak/noisy rows are filtered more explicitly before signal generation
- local tests pass

## Test Considerations
- OCR evaluation summary tests
- signal filter tests
- output summary tests where applicable
- local script smoke validation

## Documentation Updates Required
- phase doc
- module docs for any new helpers/scripts
- OCR docs if selection/fallback assumptions change

## Current Status Notes
- Phase 09 started after Phase 08 merged to main.
- Initial focus is practical OCR comparison output and quality-aware signal tightening rather than large parser rewrites.
