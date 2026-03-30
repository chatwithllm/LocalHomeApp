# Phase 06 — Output and Integration

## Objective
Deliver structured summaries, reports, and exports from LocalHomeApp in a privacy-safe, user-meaningful way.

## Scope
- output models
- local report building
- purchase history export
- Telegram-friendly summary formatting
- output runtime orchestration

## Out of Scope
- dashboards/web UI
- cloud sync
- broad third-party integrations
- raw receipt redistribution

## Deliverables
- output models
- local report builder
- purchase history exporter
- Telegram summary formatter
- output runtime service
- initial implementation pack with docs and baseline tests

## Risks
- oversharing sensitive receipt content
- coupling outputs too tightly to one surface
- unreadable or noisy user-facing summaries

## Dependencies
- Phase 4 storage layer
- Phase 5 signal layer

## Acceptance Criteria
- structured outputs can be assembled from stored data/signals
- user-facing summaries remain concise and privacy-safe
- exports are locally usable and documented
- local tests pass

## Test Considerations
- output model tests
- formatter tests
- exporter tests
- report builder tests
- runtime orchestration tests

## Documentation Updates Required
- phase doc
- output module docs
- operations docs if output flow expands

## Current Status Notes
- Phase 6 planning has started.
- Output scaffolds have begun with models, builders, formatters, exporters, runtime orchestration, and baseline tests.
- A real SQLite-backed output demo path and output operations documentation have now been added so output usefulness can be judged against actual stored history and current signals.
