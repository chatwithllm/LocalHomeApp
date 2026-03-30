# Phase 02 — Dual Local OCR

## Objective
Implement a dual local OCR strategy that supports both Apple-optimized execution and portable cross-machine OCR.

## Scope
- OCR interface definition
- Apple-oriented OCR engine integration
- portable OCR engine integration
- OCR preprocessing baseline
- OCR result persistence
- comparative evaluation notes

## Out of Scope
- full receipt parsing
- recommendation logic
- cloud OCR fallback

## Deliverables
- OCR abstraction layer
- primary Apple-oriented OCR implementation
- portable OCR implementation
- OCR result schema
- OCR evaluation and decision notes

## Risks
- image quality variability
- OCR inconsistency across stores
- machine-specific dependency behavior

## Dependencies
- local artifact intake pipeline
- sensitive local storage root
- technology decision record for OCR

## Acceptance Criteria
- both OCR engines run locally
- OCR outputs are persisted with provenance
- engine selection is configuration-driven
- no OCR data leaves local storage

## Test Considerations
- fixture-based OCR runs
- preprocessing tests
- OCR comparison cases
- failure classification tests

## Documentation Updates Required
- technology decisions
- OCR architecture docs
- module docs
- setup docs
