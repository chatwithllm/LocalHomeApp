# Phase 03 — Receipt Parsing

## Objective
Transform OCR text into structured grocery receipt data with explicit confidence and validation handling.

## Scope
- parse result models
- merchant/format detection
- receipt header extraction
- line-item extraction boundary
- parse validation rules
- parse runtime orchestration

## Out of Scope
- recommendation logic
- price forecasting
- inventory inference
- cloud parsing services

## Deliverables
- parse result models
- merchant/format detector
- header extraction module
- line-item extraction module
- parse validation module
- parse runtime service
- initial implementation pack with scaffolds, docs, and baseline tests

## Risks
- OCR noise leading to weak parsing
- merchant format variation
- overconfident structured output from noisy text

## Dependencies
- Phase 1 intake backend
- Phase 2 OCR outputs
- real OCR text fixtures

## Acceptance Criteria
- receipt-level fields can be extracted into a structured model
- parse confidence/validation states are explicit
- parsing logic is documented and locally tested

## Test Considerations
- parse model tests
- header extraction tests
- line-item boundary tests
- validation tests
- OCR-text fixture tests

## Documentation Updates Required
- phase doc
- module docs
- architecture docs if parse flow shifts

## Current Status Notes
- Phase 3 planning has started.
- Parsing scaffolds have begun with models, header extraction, line-item boundary, validation, and runtime orchestration.
- Parse result storage, real OCR-text fixture coverage, and improved subtotal/tax extraction have now been added as the next implementation slice.
- Line-item extraction now captures basic price totals and confidence hints, parse validation now emits confidence/notes, and a controlled real parse run script now persists structured output locally.
- Store-location boilerplate filtering has been tightened further (for example city/state lines such as `COLUMBUS, IN`) based on real parse validation feedback.
- Merchant detection now covers Walmart, Micro Center, and Meijer; total extraction can fall back from payment lines and tolerate OCR-spaced decimals; retail metadata filtering was tightened further for receipts with customer/CSR/sales-reference sections.
