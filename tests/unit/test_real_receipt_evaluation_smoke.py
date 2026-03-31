from pathlib import Path

from local_home_app.ocr.apple_vision_ocr import AppleVisionOcrEngine
from local_home_app.ocr.ocr_comparison_runner import run_ocr_comparison
from local_home_app.ocr.ocr_evaluation_summary import summarize_ocr_comparison
from local_home_app.ocr.tesseract_ocr import TesseractOcrEngine


def test_real_receipt_evaluation_summary_smoke(tmp_path: Path) -> None:
    sample = tmp_path / 'sample.txt'
    sample.write_text('not an image', encoding='utf-8')

    comparison = run_ocr_comparison(
        intake_id='phase-09-smoke',
        source_artifact_path=sample,
        variants=[
            ('apple_vision', AppleVisionOcrEngine()),
            ('tesseract_raw', TesseractOcrEngine(preprocess=False)),
        ],
    )
    summary = summarize_ocr_comparison(comparison)
    assert summary.intake_id == 'phase-09-smoke'
    assert len(summary.entries) == 2
