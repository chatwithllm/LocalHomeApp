"""Run one controlled OCR comparison for LocalHomeApp Phase 2."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.ocr.ocr_comparison_runner import run_ocr_comparison
from local_home_app.ocr.ocr_comparison_store import OcrComparisonStore
from local_home_app.ocr.tesseract_ocr import TesseractOcrEngine


def main() -> None:
    source_artifact_path = Path("/Users/assistant/.openclaw/media/inbound/file_0---90663f28-4ac5-4d8e-8a7b-0c64776e1f73.jpg")
    comparison = run_ocr_comparison(
        intake_id="manual-phase-02-comparison",
        source_artifact_path=source_artifact_path,
        variants=[
            ("tesseract_raw", TesseractOcrEngine(preprocess=False)),
            (
                "tesseract_preprocessed",
                TesseractOcrEngine(
                    preprocess=True,
                    preprocessed_output_dir=Path("/Users/assistant/LocalHomeAppSensitiveData/ocr_outputs/preprocessed"),
                ),
            ),
        ],
    )

    store = OcrComparisonStore(
        Path("/Users/assistant/LocalHomeAppSensitiveData/ocr_outputs/ocr_comparisons.jsonl")
    )
    store.append(comparison)

    print(f"comparison_id={comparison.comparison_id}")
    for entry in comparison.entries:
        print(f"label={entry.label}")
        print(f"status={entry.result.status}")
        print(f"runtime_ms={entry.result.runtime_ms}")
        print(f"preprocessed_artifact_path={entry.result.preprocessed_artifact_path}")
        print("text_start")
        print(entry.result.ocr_text[:2000])
        print("text_end")


if __name__ == "__main__":
    main()
