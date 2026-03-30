# OCR Operations

## Purpose
Describe how OCR is currently operated and validated in LocalHomeApp.

## Current operational flow
1. Receipt artifact exists locally.
2. Optional preprocessing generates an OCR-friendly image copy.
3. Selected OCR engine runs locally.
4. OCR result is captured in a structured record.
5. OCR result is persisted locally.

## Current implemented engine behavior
### Tesseract
- returns `completed` when OCR succeeds
- returns `failed` when command execution fails
- returns `not_available` when the binary is not present
- currently defaults to preprocessing for image-based inputs

## Current comparison observation
A real raw-vs-preprocessed Tesseract comparison was run against a local receipt image during Phase 2. On that sample, preprocessing produced a cleaner OCR result and a slightly faster runtime than the raw image path. Until contradicted by broader fixtures, preprocessing should remain the default Tesseract behavior.

### Apple-oriented OCR
- currently returns `not_available` until the macOS-native bridge is implemented

## Current local storage artifacts
- OCR result store: `ocr_outputs/ocr_results.jsonl`
- preprocessed images: local sensitive OCR storage as created by preprocessing workflows

## Operational validation standard
Before considering an OCR phase slice stable:
- local tests must pass
- a real local OCR run should be exercised when feasible
- docs must be updated to reflect what actually worked and what is still pending
