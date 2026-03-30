# Product Requirements Document (PRD) — LocalHomeApp

## 1. Product Summary
LocalHomeApp is a privacy-first grocery receipt intelligence system for real household use. The system accepts grocery receipts through Telegram as the primary V1 intake channel, downloads them to local machine-controlled storage, performs local-only OCR, extracts structured purchase data, stores purchase history locally, and generates inventory and price intelligence from buying patterns.

The project is designed as a production-quality local system rather than a throwaway prototype. It prioritizes correctness, privacy, portability, maintainability, and disciplined phased delivery.

## 2. Product Goals
1. Accept grocery receipts through Telegram.
2. Download and persist raw receipt inputs locally.
3. Perform OCR locally only.
4. Extract structured grocery purchase data with traceability.
5. Store purchase history locally for household use.
6. Generate inventory signals, replenishment hints, and price expectations.
7. Send only structured outputs to downstream surfaces when needed.
8. Keep the system portable so it can move to a different machine later.

## 3. Non-Goals for V1
- No cloud OCR.
- No requirement for a web dashboard in V1.
- No broad multi-user or multi-tenant model.
- No silent export of raw receipts outside the local system.
- No uncontrolled expansion beyond grocery receipt intelligence.

## 4. Operating Principles
- Privacy first.
- Local-first storage for sensitive artifacts.
- GitHub is the source of truth for non-sensitive code and documentation.
- Raw receipts, OCR text, local databases, and sensitive operational data remain outside Git-tracked storage.
- Development is phase-based.
- Every phase must be documented before it is considered complete.
- Deviation from the PRD must be explicitly documented and approved through a documented change record.

## 5. Primary Users and Channels
### Primary user
- Household operator / owner.

### Primary intake channel
- Telegram bot.
- In the current deployment model, Telegram ingress is owned by OpenClaw, which serves as the active Telegram-facing runtime.
- LocalHomeApp acts as the local processing backend behind that ingress boundary.

### Telegram channel model for V1
- **Main chat**: user commands, approvals, user-facing summaries.
- **Workers chat**: OCR/parser/ingestion/sub-worker operational context.
- **Alerts chat**: failures, manual review requests, operational alerts.

This separation exists to preserve context quality in the main chat and to keep worker-system noise contained.

## 6. Data Privacy Requirements
- Raw receipt images/documents must remain on local machine-controlled storage.
- OCR must execute locally only.
- GitHub must contain only non-sensitive code and documentation.
- Outputs sent to Telegram or other downstream surfaces should be structured summaries, not raw receipt artifacts, unless explicitly designed and approved.
- Secrets must be stored outside Git-tracked files.

## 7. V1 Functional Requirements
1. Receive receipt images/documents via Telegram.
2. Download receipt inputs to local storage.
3. Track intake metadata and provenance.
4. Run dual local OCR strategy:
   - **Primary OCR** optimized for Apple Silicon / Mac mini M4.
   - **Secondary OCR** selected for portability and reliability across machines.
5. Store OCR output locally.
6. Parse structured receipt data.
7. Persist structured purchases locally.
8. Generate initial inventory and price intelligence.
9. Send structured summaries/alerts to the appropriate Telegram channels.

## 8. Dual OCR Requirement
The system must implement two local OCR paths:
- **Primary Apple-oriented OCR**: optimized for the Mac mini M4 / Apple Silicon environment.
- **Portable OCR fallback/alternative**: runs well on broader environments and provides a portability/resilience path.

Selection, fallback rules, and comparative quality evaluation must be documented. Both OCR options must remain local-only.

## 9. Architecture Constraints
- CLI-first runtime for V1.
- Configuration-driven paths and environment settings.
- Machine-specific assumptions must be isolated in documentation and configuration.
- Source code must use clear, production-appropriate names.
- Every Python file must have module-level documentation in `docs/modules/`.

## 10. Quality Requirements
- Production-style repository structure.
- Meaningful commits.
- Feature branches and pull requests.
- Stable tests for core workflows.
- Regression fixtures for parsing and OCR-sensitive cases.
- Documentation updates required for every phase and materially important module.
- Phase completion requires passing documented acceptance criteria, including required local tooling and baseline test execution where applicable.
- If a phase is partially scaffolded but not yet locally verified, that incomplete status must be recorded explicitly in the phase document.
- Every phase must be tested locally before it is considered ready.
- After local testing passes, each phase must proceed on its own dedicated branch, with updated documentation and a phase-specific commit before merge approval is requested.

## 11. Change Control / PRD Deviation Policy
The project must not casually drift beyond its defined objective.

If a requirement, scope boundary, architecture direction, or operating principle needs to change:
1. create a documented PRD change record,
2. explain the reason,
3. document alternatives considered,
4. identify privacy, portability, and maintenance impact,
5. update affected architecture/phase docs,
6. explicitly note the decision in the roadmap or ADR set.

No significant deviation should be treated as informal.

## 12. Success Criteria
- The system reliably ingests grocery receipts from Telegram.
- Sensitive receipt artifacts stay local.
- OCR and parsing produce usable structured purchase history.
- The household can derive trustworthy grocery intelligence from historical data.
- The system remains understandable, maintainable, and portable.
