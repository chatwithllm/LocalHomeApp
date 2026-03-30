from local_home_app.ocr.ocr_result_models import OcrResultRecord


def test_ocr_result_record_fields() -> None:
    record = OcrResultRecord(
        ocr_run_id="ocr-001",
        intake_id="intake-001",
        engine_name="apple_vision",
        engine_version="1.0",
        source_artifact_path="/tmp/receipt.jpg",
        preprocessed_artifact_path=None,
        ocr_text="TOTAL 12.34",
        confidence_summary=None,
        runtime_ms=125,
        status="completed",
    )

    assert record.engine_name == "apple_vision"
    assert record.status == "completed"
