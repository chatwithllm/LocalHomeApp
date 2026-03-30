from pathlib import Path

from local_home_app.ocr.ocr_result_models import OcrResultRecord
from local_home_app.ocr.ocr_result_store import OcrResultStore


def test_ocr_result_store_append_and_load(tmp_path: Path) -> None:
    store = OcrResultStore(tmp_path / "ocr_results.jsonl")
    record = OcrResultRecord(
        ocr_run_id="ocr-001",
        intake_id="intake-001",
        engine_name="tesseract",
        engine_version=None,
        source_artifact_path="/tmp/receipt.jpg",
        preprocessed_artifact_path=None,
        ocr_text="TOTAL 12.34",
        confidence_summary=None,
        runtime_ms=100,
        status="completed",
    )

    store.append(record)
    loaded = store.load_all()

    assert len(loaded) == 1
    assert loaded[0].ocr_text == "TOTAL 12.34"
