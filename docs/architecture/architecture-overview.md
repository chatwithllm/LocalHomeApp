# Architecture Overview

## Purpose
LocalHomeApp is a local-first grocery receipt intelligence system with Telegram as V1 intake and local-only OCR.

## High-Level Flow
1. Receipt arrives through Telegram.
2. OpenClaw owns Telegram ingress and receives the inbound update.
3. LocalHomeApp intake processing receives a normalized or handed-off receipt input from OpenClaw.
4. Intake layer stores the artifact to local machine-controlled storage.
5. Metadata about the intake event is persisted.
6. OCR pipeline runs locally using one of two local OCR engines.
7. OCR text is stored locally and linked to source artifacts.
8. Parsing pipeline extracts structured grocery purchase data.
9. Structured data is stored in SQLite with provenance.
10. Signal generation computes inventory and price intelligence.
11. Structured summaries/alerts route to Telegram chats by purpose.

## Ingress Ownership
In the current architecture, OpenClaw is the Telegram ingress owner. LocalHomeApp should not assume standalone ownership of Telegram polling for the same bot in this deployment model.

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
