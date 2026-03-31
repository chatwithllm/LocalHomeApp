# Module: ocr_evaluation_summary.py

## Purpose
Turn raw OCR comparison results into a practical summary for inspection, testing, and local evaluation notes.

## Inputs
Structured OCR comparison records.

## Outputs
Structured OCR evaluation summary objects and rendered text summaries.

## Dependencies
- dataclasses
- typing
- ocr_comparison_models

## Execution Context
Used by Phase 09 OCR evaluation workflows and local comparison scripts.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- empty or weak OCR comparison records yield sparse summaries

## Related Tests
- tests/unit/test_ocr_evaluation_summary.py

## Related Docs
- docs/phases/phase-09-real-receipt-evaluation.md
