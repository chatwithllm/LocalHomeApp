# LocalHomeApp Roadmap

## Phase 00 — Foundation
Repository structure, documentation baseline, configuration model, naming standards, quality tooling, architecture skeleton.

## Phase 01 — Telegram Intake
Telegram bot integration, receipt download flow, intake metadata, local storage boundaries, chat/channel routing rules.

## Phase 02 — Dual Local OCR
Implement Apple-optimized local OCR and portable local OCR, preprocessing, OCR result persistence, quality comparison strategy.

## Phase 03 — Structured Receipt Parsing
Receipt parsing, merchant/format detection, line item extraction, validation rules, confidence handling.

## Phase 04 — Local Storage and History
SQLite schema, migrations, repositories, purchase history model, provenance tracking.

## Phase 05 — Grocery Intelligence
Inventory signals, repeat purchase intervals, price expectations, anomaly hints, explainable recommendations.

## Phase 06 — Output and Telegram Delivery
Structured summaries, worker/alert routing, export contracts, output privacy controls.

## Phase 07 — Hardening and Portability
Operational runbook, backup/restore, machine migration, service/process discipline, portability validation.

## Scope Governance
Any major deviation from this roadmap or the PRD must be documented through PRD change control and linked documentation updates.
