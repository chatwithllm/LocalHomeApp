# Phase 01 — Telegram Intake

## Objective
Implement reliable Telegram-based receipt intake for LocalHomeApp using the established Main, Workers, and Alerts channel model.

## Scope
- Telegram bot intake flow
- local download of receipt artifacts
- intake metadata capture
- routing rules for Main, Workers, Alerts
- duplicate receipt intake handling baseline

## Out of Scope
- OCR execution
- structured parsing
- recommendation logic

## Deliverables
- Telegram intake modules
- local receipt artifact storage rules
- intake metadata schema
- intake operational documentation
- initial implementation pack with module scaffolds, docs, and baseline tests

## Current Status Notes
- Phase 1 implementation scaffolding has started.
- Telegram receipt normalization, local artifact path planning, intake metadata model, duplicate detection helper, and an intake service entry script scaffold have been created.
- File hashing and intake metadata construction helpers have now been added as the next implementation slice.
- A temporary JSONL-backed local intake metadata store and an end-to-end local intake orchestration helper have now been added for early Phase 1 persistence and workflow validation.
- A real Telegram download boundary and runtime intake service helper have now been added to connect Telegram file retrieval to the local intake workflow.
- Receipt validation rules, centralized intake status values, and worker/alert event formatting helpers have now been added to make the intake path safer and more operationally explicit.
- Validation, rejected-candidate handling, failed-download handling, and worker/alert message outputs are now wired into the runtime intake flow.
- Telegram update extraction, live runtime integration helpers, and routing-ready output construction have now been added so receipt-like updates can flow from raw Telegram payloads to channel-ready messages.
- A polling/update-consumption loop skeleton and minimal delivery payload construction have now been added, bringing the Phase 1 runtime architecture close to operational intake.
- The intake service entry point now supports a controlled single-pass polling run for real-world Phase 1 validation before closeout.
- Real-world validation exposed a direct-script src-layout import-path issue in the runtime entry point; this has to be resolved before Phase 1 can be considered operationally verified.
- Baseline Phase 1 unit tests should be kept passing as implementation expands.

## Risks
- duplicate uploads
- unsupported file formats
- Telegram channel behavior edge cases

## Dependencies
- functioning Telegram bot configuration
- documented local sensitive storage root
- configuration model

## Acceptance Criteria
- receipt inputs can be received and handed off from the Telegram ingress layer to LocalHomeApp intake processing
- intake metadata is stored with provenance
- worker and alert routing boundaries are clear
- the architecture clearly documents ingress ownership to avoid competing Telegram polling assumptions

## Test Considerations
- mocked Telegram updates
- duplicate detection tests
- local artifact persistence tests
- ingress handoff design validation

## Documentation Updates Required
- PRD
- Telegram setup
- architecture data flow
- architecture overview
- ADR set
- module docs

## Current Phase Boundary Clarification
Operational validation showed that direct standalone polling by LocalHomeApp is not the correct ingress model for the currently deployed bot, because OpenClaw already owns Telegram ingress. Phase 1 should therefore be judged against a documented OpenClaw-to-LocalHomeApp handoff model rather than a competing standalone polling assumption.
