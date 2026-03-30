# Phase 00 — Foundation

## Objective
Establish the LocalHomeApp repository, documentation baseline, architecture skeleton, naming standards, and configuration model for disciplined development.

## Scope
- Repository scaffold
- Core documents
- Configuration templates
- Initial package layout
- Quality tooling baseline
- Phase governance and PRD change-control policy

## Out of Scope
- Live Telegram integration
- OCR execution
- Receipt parsing
- Local database implementation

## Deliverables
- Initial repository structure
- PRD
- roadmap
- architecture overview
- standards docs
- phase documentation skeleton
- base Python package layout

## Risks
- Loose early structure causing future drift
- Under-documenting scope boundaries
- Allowing sensitive data into Git-tracked areas

## Dependencies
- Repository access
- Agreement on CLI-first V1
- Agreement on local-only storage of sensitive data

## Acceptance Criteria
- Repository scaffold exists.
- PRD captures channel model, privacy rules, and dual OCR requirement.
- Roadmap exists with clear phases.
- Architecture and standards docs are in place.
- Sensitive/local data boundaries are documented.
- Foundational Python modules exist for settings, logging, filesystem paths, and runtime errors.
- Local quality tooling is installed and baseline unit tests run successfully.

## Current Status Notes
- Repository scaffold, PRD, roadmap, architecture docs, standards docs, ADRs, foundational modules, and initial unit tests have been created.
- Telegram Main/Workers/Alerts channel model and local sensitive storage root have been documented.
- Local Python quality tooling has been installed in `.venv`.
- Initial baseline test execution exposed a src-layout packaging/import-path gap; this is part of Phase 0 acceptance work and must be resolved before the phase is considered complete.
- Subsequent baseline testing exposed a Python-version alignment issue between the local environment and project code expectations; this must be resolved and documented as part of Phase 0.
- Baseline testing also exposed a deterministic logging-configuration behavior gap; fixing runtime/test reliability is part of Phase 0 acceptance work.
- Phase 0 is not complete until the baseline unit tests pass.

## Test Considerations
- Basic project import check
- Config-loading tests once implemented
- Lint/test toolchain setup validation
- Baseline unit test execution for foundational modules

## Documentation Updates Required
- README
- PRD
- ROADMAP
- architecture overview
- naming conventions
- technology decision records
- phase status notes when acceptance criteria are partially complete
