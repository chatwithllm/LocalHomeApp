# ADR-0001 — Project Structure

## Status
Accepted

## Context
LocalHomeApp requires a production-style project structure with clear separation between code, docs, config templates, tests, and sensitive local runtime data.

## Decision
Adopt a repository structure that keeps:
- source code under `src/`
- documentation under `docs/`
- tests under `tests/`
- reusable scripts under `scripts/`
- non-sensitive config templates under `config/`
- sensitive runtime artifacts outside the repository

## Consequences
- improved maintainability
- clearer Git boundaries
- easier portability and onboarding
