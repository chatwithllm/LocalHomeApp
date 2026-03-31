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
- initial Phase 2 implementation pack with OCR interface/result scaffolding and baseline tests

## Current Status Notes
- Phase 2 planning has started.
- Dual local OCR strategy is now explicitly documented via ADR.
- OCR result and interface scaffolding have been added.
- Apple-oriented OCR, portable OCR, and preprocessing boundaries are now scaffolded for the next implementation slices.
- OCR result storage has now been added, and the Tesseract path now has a first real execution implementation with explicit not-available and failed states.
- Basic local preprocessing now exists for image-based OCR inputs and is wired into the Tesseract path, including preprocessed artifact generation even when the OCR binary is unavailable.
- The Apple-oriented OCR path now runs through a real macOS-native Swift/Vision bridge that is compiled locally on demand from the repo and executed against local image artifacts.
- OCR setup and operations documentation now reflect the current verified Tesseract runtime, preprocessing behavior, local OCR storage, and the Swift/Vision bridge path for Apple OCR.
- An OCR comparison harness has now been added so raw/preprocessed and future cross-engine comparisons can be represented and persisted locally.
- A real raw-vs-preprocessed Tesseract comparison was run against a local receipt image; preprocessing produced a cleaner and faster result on the tested sample and should remain the default Tesseract path for now.
- The Apple Vision path has now been validated locally through the native Swift/Vision bridge on this machine; a simple local image test completed successfully and returned structured OCR text.
- The remaining operational expectation is to validate the Apple Vision path against additional real receipt artifacts and document any observed selection/fallback preference relative to Tesseract.

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
