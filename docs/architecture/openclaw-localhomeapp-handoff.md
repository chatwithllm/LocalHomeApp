# OpenClaw → LocalHomeApp Handoff Design

## Purpose
Define the current intended boundary between Telegram ingress and LocalHomeApp local receipt processing.

## Ownership model
- OpenClaw owns Telegram ingress.
- LocalHomeApp owns local receipt-intake processing, persistence, and later OCR/parsing/signal generation.

## Handoff responsibility
OpenClaw should hand LocalHomeApp the receipt intake input in a normalized form that preserves:
- source channel (`telegram`)
- chat ID
- message ID
- user ID
- media identity information
- local or downloaded receipt artifact bytes/path
- timing/provenance metadata

## Why this boundary exists
- avoids competing Telegram polling consumers for the same bot
- aligns with the current deployed runtime setup
- keeps LocalHomeApp focused on privacy-first local processing

## Expected Phase 1 outcome
Phase 1 should deliver a robust local intake backend and a clear handoff contract, even if Telegram polling is operationally owned by OpenClaw in the deployed system.
