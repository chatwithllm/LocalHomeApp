# ADR-0002 — Telegram Channel Model

## Status
Accepted

## Context
LocalHomeApp uses Telegram as the primary V1 channel and needs to preserve context quality in the main user interaction surface while still supporting worker and alert traffic.

## Decision
Use a single Telegram bot with three surfaces:
- Main DM for user interaction and approvals
- Workers private group for operational context
- Alerts private group for failures and manual review

## Consequences
- simpler token and identity management
- cleaner operational separation
- easier OpenClaw routing compared with multiple bots
