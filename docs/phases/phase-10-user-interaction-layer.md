# Phase 10 — User Interaction Layer

## Objective
Provide a practical user-facing query layer so LocalHomeApp data can be accessed through concise questions and summaries rather than only developer scripts.

## Scope
- query-oriented history access helpers
- merchant and item lookup summaries
- recent receipt summaries for messaging/conversational use
- a local interaction script for common questions
- baseline tests and docs

## Out of Scope
- full web dashboard
- authentication/multi-user support
- advanced natural-language interpretation
- manual review UI

## Deliverables
- phase doc
- interaction/query service module
- merchant/item history query support
- recent receipt summary support
- local interaction script
- module docs and tests

## Risks
- weak upstream parsing limits answer quality
- simplistic query handling may need later refinement
- database contents may be sparse during early testing

## Dependencies
- local storage layer
- parse outputs and purchase history repository
- output formatting conventions

## Acceptance Criteria
- recent receipts can be summarized for user-facing answers
- merchant/item filters can produce useful local query results
- a local script can answer basic questions from stored data
- local tests pass

## Test Considerations
- repository query tests
- interaction service tests
- local script smoke validation where feasible

## Documentation Updates Required
- phase doc
- module docs for new interaction service
- usage notes for the local interaction script

## Current Status Notes
- Phase 10 begins after Costco parsing improvements and Phase 09 evaluation work.
- Initial emphasis is a useful conversational/query layer, not a dashboard.
