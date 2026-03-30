from local_home_app.ocr.ocr_comparison_models import OcrComparisonEntry, OcrComparisonRecord
from local_home_app.ocr.ocr_result_models import OcrResultRecord


def test_ocr_comparison_record_fields() -> None:
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
    entry = OcrComparisonEntry(label="raw", result=result)
    record = OcrComparisonRecord(comparison_id="cmp-001", intake_id="intake-001", entries=[entry])

    assert record.entries[0].label == "raw"
