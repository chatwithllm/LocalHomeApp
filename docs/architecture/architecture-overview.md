# Architecture Overview

## Purpose
LocalHomeApp is a local-first grocery receipt intelligence system with Telegram as V1 intake and local-only OCR.

## High-Level Flow
1. Receipt arrives through Telegram.
2. Intake layer downloads the artifact to local machine-controlled storage.
3. Metadata about the intake event is persisted.
4. OCR pipeline runs locally using one of two local OCR engines.
5. OCR text is stored locally and linked to source artifacts.
6. Parsing pipeline extracts structured grocery purchase data.
7. Structured data is stored in SQLite with provenance.
8. Signal generation computes inventory and price intelligence.
9. Structured summaries/alerts route to Telegram chats by purpose.

## Chat Separation Model
- Main chat: operator-facing interaction and approvals.
- Workers chat: background operational context, worker messages, sub-worker logs.
- Alerts chat: failures and action-required signals.

## Privacy Boundary
Sensitive artifacts remain local:
- raw receipts
- OCR text
- local database
- exported local datasets unless explicitly approved

GitHub contains only non-sensitive code and documentation.

## Runtime Shape
- CLI-first execution model for V1.
- Background workers/processes may later be supervised, but naming and process identity must remain explicit and human-readable.

## Portability Rules
- All pathing is configuration-driven.
- OCR engines are abstracted behind a common interface.
- Machine-specific setup belongs in setup docs, not business logic.
