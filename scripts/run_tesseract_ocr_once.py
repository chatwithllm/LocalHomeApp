"""Run one controlled Tesseract OCR test for LocalHomeApp Phase 2."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.ocr.ocr_result_store import OcrResultStore
from local_home_app.ocr.tesseract_ocr import TesseractOcrEngine


def main() -> None:
    source_artifact_path = Path("/Users/assistant/.openclaw/media/inbound/file_0---90663f28-4ac5-4d8e-8a7b-0c64776e1f73.jpg")
    result = TesseractOcrEngine().run_ocr(
        intake_id="manual-phase-02-test",
        source_artifact_path=source_artifact_path,
    )

    store = OcrResultStore(
        Path("/Users/assistant/LocalHomeAppSensitiveData/ocr_outputs/ocr_results.jsonl")
    )
    store.append(result)

    print(f"status={result.status}")
    print(f"engine={result.engine_name}")
    print(f"runtime_ms={result.runtime_ms}")
    print("text_start")
    print(result.ocr_text[:4000])
    print("text_end")


if __name__ == "__main__":
    main()
