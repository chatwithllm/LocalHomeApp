# ADR-0004 — OpenClaw Owns Telegram Ingress

## Status
Accepted

## Context
LocalHomeApp uses a Telegram bot that is already actively connected to OpenClaw. During Phase 1 operational validation, standalone LocalHomeApp polling against the same bot did not receive the fresh receipt updates, even after runtime configuration issues were fixed. This strongly suggests that Telegram ingress ownership already belongs to OpenClaw in the current deployment model.

Running two separate polling consumers against the same Telegram bot creates ambiguity, possible update-consumption conflicts, and unnecessary operational complexity.

## Decision
OpenClaw will own Telegram ingress for the current LocalHomeApp architecture.

LocalHomeApp will act as the local receipt-intake processing backend, receiving normalized or handed-off receipt inputs from OpenClaw rather than directly competing for Telegram updates from the same bot.

## Consequences
### Positive
- cleaner ingress ownership
- avoids polling conflicts
- aligns with the existing deployed bot setup
- keeps LocalHomeApp focused on local processing, persistence, and later OCR/parsing logic

### Tradeoffs
- LocalHomeApp is not the direct Telegram polling owner in this deployment model
- a handoff boundary from OpenClaw to LocalHomeApp must be defined and documented

## Follow-up
- update PRD and architecture docs
- adjust Phase 1 completion criteria to reflect OpenClaw-owned Telegram ingress
- define the OpenClaw-to-LocalHomeApp handoff contract
