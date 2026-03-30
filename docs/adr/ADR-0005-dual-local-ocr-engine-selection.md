# ADR-0005 — Dual Local OCR Engine Strategy

## Status
Accepted (initial strategy)

## Context
LocalHomeApp requires local-only OCR with two goals that naturally compete:
- optimize for the current Mac mini / Apple Silicon environment
- remain portable to other machines later

A single hardwired OCR engine would either sacrifice local optimization or weaken portability.

## Decision
LocalHomeApp will support two local OCR paths:
1. Apple-oriented OCR implementation for the current Apple hardware environment
2. Portable OCR implementation for broader machine portability

The initial planned direction is:
- Apple-oriented OCR: Apple Vision-based path
- Portable OCR: Tesseract-based path

Both must remain local-only and must be accessed through a shared OCR interface.

## Consequences
### Positive
- better optimization for the current hardware
- clearer portability story
- easier comparative evaluation later

### Tradeoffs
- increased implementation complexity
- more documentation and testing responsibility

## Follow-up
- define OCR result models
- define OCR engine interface
- document setup requirements for both OCR paths
