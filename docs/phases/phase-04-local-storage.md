# Phase 04 — Local Storage and Purchase History

## Objective
Create a durable, queryable local storage layer for receipt intake events, OCR results, structured parse outputs, and purchase history.

## Scope
- database connection layer
- storage schema
- migration runner
- repositories for intake, OCR, parses, and purchase history
- provenance linking across pipeline stages

## Out of Scope
- recommendations
- inventory inference
- analytics/dashboard
- cloud sync

## Deliverables
- database connection module
- storage schema module
- migration runner module
- repository scaffolds
- initial implementation pack with docs and tests

## Risks
- schema drift across phases
- weak provenance linkage
- overcomplicating storage too early

## Dependencies
- Phase 1 intake backend
- Phase 2 OCR outputs
- Phase 3 structured parses

## Acceptance Criteria
- local database schema can be created
- core repositories exist with documented responsibilities
- storage layer preserves provenance relationships
- local storage tests pass

## Test Considerations
- schema creation tests
- repository CRUD tests
- provenance linkage tests
- fixture-backed storage tests

## Documentation Updates Required
- phase doc
- storage module docs
- architecture/storage docs if needed

## Current Status Notes
- Phase 4 planning has started.
- Storage scaffolds have begun with connection, schema, migrations, repositories, and provenance-preserving tests.
- A controlled SQLite persistence demo path and database operations documentation have now been added for real storage validation.
- A simple purchase history summary path now proves that data can be queried back from SQLite in a meaningfully usable form.
