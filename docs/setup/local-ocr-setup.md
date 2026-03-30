# Local OCR Setup

## Purpose
Document how LocalHomeApp will support dual local OCR while keeping all OCR execution on the local machine.

## OCR strategy
LocalHomeApp will support two local OCR paths:

1. **Apple-oriented OCR**
   - intended for Mac mini / Apple Silicon optimization
   - likely direction: Apple Vision-based implementation

2. **Portable OCR**
   - intended for broader machine portability
   - initial direction: Tesseract

## Why two OCR paths
- optimize for current Apple hardware
- preserve portability to future machines
- allow comparative evaluation for quality and reliability

## Local-only rule
OCR execution must remain local. No receipt OCR content should be sent to external OCR providers.

## Setup requirements to document further in Phase 02
- Apple OCR runtime dependency requirements
- Tesseract installation instructions
- preprocessing/image normalization prerequisites
- OCR engine selection via configuration
- OCR comparison workflow for test receipts

## Current Phase 0 note
This document records the intended setup and decision direction. Final engine installation and operational steps will be completed during Phase 02.
