# Local OCR Setup

## Purpose
Document how LocalHomeApp runs local-only OCR in the current environment and what remains to be implemented.

## Current OCR strategy
LocalHomeApp supports two local OCR paths:

1. **Apple-oriented OCR path**
   - represented through a macOS-native bridge boundary
   - intended for Apple hardware optimization
   - actual bridge implementation is not yet connected in the current Python environment

2. **Portable OCR path (Tesseract)**
   - implemented and working locally
   - currently the first real OCR execution path in the project

## Verified local state
### Tesseract
- installed on this machine
- verified version during Phase 2 work: `5.5.2`
- available at: `/opt/homebrew/bin/tesseract`
- LocalHomeApp successfully ran a real OCR test against a local receipt image

### Apple-oriented OCR
- Apple framework bindings were not available in the current Python environment
- current project design uses a bridge boundary so the Apple path can be connected later without breaking the OCR interface

## Current OCR storage
OCR results are currently persisted locally at:
- `/Users/assistant/LocalHomeAppSensitiveData/ocr_outputs/ocr_results.jsonl`

Preprocessed OCR artifacts should remain under local sensitive storage as Phase 2 expands.

## Current preprocessing behavior
For image-based OCR inputs, LocalHomeApp currently:
- creates a grayscale copy
- applies autocontrast
- saves a preprocessed PNG artifact
- passes that preprocessed image to Tesseract when preprocessing is enabled

## Current local test command
Example controlled local OCR test:

```bash
. .venv/bin/activate
python scripts/run_tesseract_ocr_once.py
```

## Current known limitations
- Apple OCR bridge not yet implemented
- OCR comparison workflow not yet built
- preprocessing is intentionally basic in the current phase
- OCR persistence is JSONL-backed for now, not yet database-backed
