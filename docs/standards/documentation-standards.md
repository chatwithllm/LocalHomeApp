# Documentation Standards

## Continuous documentation rule
Documentation must be updated continuously throughout development. No phase is complete until code, tests, and documentation are aligned.

## Required documentation categories
- project-level documents
- phase documents
- architecture documents
- setup/operations documents
- technology decision documents
- module-level documents

## Module documentation rule
Every Python file must have a corresponding document in `docs/modules/` describing:
- purpose
- inputs
- outputs
- dependencies
- execution context
- required permissions
- expected errors/failure modes
- related tests
- related docs

## PRD deviation rule
Any meaningful deviation from the PRD must be documented through updated docs and an explicit change record or ADR.
