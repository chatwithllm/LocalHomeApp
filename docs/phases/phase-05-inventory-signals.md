# Phase 05 — Inventory Signals and Price Intelligence

## Objective
Generate useful, explainable grocery signals from local purchase history, including repeat-purchase patterns, price expectations, and replenishment hints.

## Scope
- signal/result models
- purchase pattern analysis
- price expectation heuristics
- inventory/reorder signal generation
- recommendation formatting

## Out of Scope
- meal planning
- advanced predictive modeling
- cloud analytics
- complex dashboards

## Deliverables
- signal models
- purchase pattern analyzer
- price expectation engine
- inventory signal generator
- recommendation formatter
- initial implementation pack with docs and baseline tests

## Risks
- overconfident inventory assumptions
- weak product normalization across noisy item names
- misleading price expectations from sparse history

## Dependencies
- Phase 4 durable local storage
- parse outputs with usable line items

## Acceptance Criteria
- signal layer can analyze purchase-history-like inputs
- price expectation and reorder hints are explainable
- local tests pass

## Test Considerations
- signal model tests
- purchase pattern analysis tests
- price expectation tests
- reorder heuristic tests

## Documentation Updates Required
- phase doc
- signal module docs
- architecture docs if signal flow shifts

## Current Status Notes
- Phase 5 planning has started.
- Signal scaffolds have begun with models, analyzers, generators, formatters, and baseline tests.
- A real SQLite-backed signal demo path and signal operations documentation have now been added so signal usefulness can be evaluated against actual stored purchase history.
- Signal input filtering and skipped-row accounting have now been added so Phase 5 can distinguish between a weak signal engine and weak parse-derived inputs.
