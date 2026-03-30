from pathlib import Path

from local_home_app.ocr.ocr_comparison_models import OcrComparisonEntry, OcrComparisonRecord
from local_home_app.ocr.ocr_comparison_store import OcrComparisonStore
from local_home_app.ocr.ocr_result_models import OcrResultRecord


def test_ocr_comparison_store_append_and_load(tmp_path: Path) -> None:
    store = OcrComparisonStore(tmp_path / "ocr_comparisons.jsonl")
    result = OcrResultRecord(
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
    record = OcrComparisonRecord(
        comparison_id="cmp-001",
        intake_id="intake-001",
        entries=[OcrComparisonEntry(label="raw", result=result)],
    )

    store.append(record)
    loaded = store.load_all()

    assert len(loaded) == 1
    assert loaded[0].comparison_id == "cmp-001"
