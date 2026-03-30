# ADR-0003 — Dual Local OCR Strategy

## Status
Accepted (initial direction)

## Context
The project must support local-only OCR while also balancing Apple Silicon optimization with future portability.

## Decision
Design LocalHomeApp with two local OCR paths:
- Apple-oriented OCR implementation for the Mac mini / Apple Silicon environment
- portable OCR implementation for broader machine support

OCR engine choice must remain configuration-driven and abstracted behind a shared interface.

## Consequences
- better local optimization on current hardware
- stronger portability story
- slightly higher implementation complexity in exchange for resilience
