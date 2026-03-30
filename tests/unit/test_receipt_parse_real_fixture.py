from pathlib import Path

from local_home_app.parsing.receipt_parse_runtime_service import run_receipt_parse


def test_run_receipt_parse_on_real_kroger_fixture() -> None:
    fixture_path = Path("tests/fixtures/kroger_ocr_sample.txt")
    text = fixture_path.read_text(encoding="utf-8")

    record = run_receipt_parse(
        intake_id="fixture-intake-001",
        ocr_run_id="fixture-ocr-001",
        ocr_text=text,
    )

    assert record.merchant_name == "Kroger"
    assert record.total == 39.04
    assert record.receipt_date == "03/15/26"
    assert record.parse_status in {"completed", "partial"}
