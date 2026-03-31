#!/usr/bin/env python3
"""Run a practical local OCR evaluation across Apple Vision and Tesseract.

Purpose:
- Execute both OCR engines against a local artifact and render a concise evaluation summary.

Inputs:
- local source artifact path
- intake identifier

Outputs:
- rendered OCR evaluation summary

Dependencies:
- argparse
- pathlib
- sys
- apple_vision_ocr
- tesseract_ocr
- ocr_comparison_runner
- ocr_evaluation_summary

Execution context:
- run manually on a local machine with available OCR engines.

Required permissions:
- local file access
- local process execution / native bridge execution

Expected errors/failure modes:
- one or both OCR engines unavailable
- unsupported local input artifact

Related docs:
- docs/modules/ocr-evaluation-summary.md
- docs/phases/phase-09-real-receipt-evaluation.md
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.ocr.apple_vision_ocr import AppleVisionOcrEngine
from local_home_app.ocr.ocr_comparison_runner import run_ocr_comparison
from local_home_app.ocr.ocr_evaluation_summary import render_ocr_evaluation_summary, summarize_ocr_comparison
from local_home_app.ocr.tesseract_ocr import TesseractOcrEngine


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local OCR evaluation across Apple Vision and Tesseract")
    parser.add_argument("source_artifact_path", help="Path to a local image artifact")
    parser.add_argument("--intake-id", default="phase-09-eval", help="Logical intake identifier")
    args = parser.parse_args()

    source_artifact_path = Path(args.source_artifact_path)
    comparison = run_ocr_comparison(
        intake_id=args.intake_id,
        source_artifact_path=source_artifact_path,
        variants=[
            ("apple_vision", AppleVisionOcrEngine()),
            ("tesseract_preprocessed", TesseractOcrEngine(preprocess=True, preprocessed_output_dir=PROJECT_ROOT / ".tmp" / "preprocessed")),
            ("tesseract_raw", TesseractOcrEngine(preprocess=False)),
        ],
    )
    summary = summarize_ocr_comparison(comparison)
    print(render_ocr_evaluation_summary(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
