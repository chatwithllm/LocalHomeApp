from local_home_app.parsing.receipt_parse_runtime_service import run_receipt_parse


def test_run_receipt_parse() -> None:
    text = "KROGER\nMILK 3.99\nBREAD 2.49\nVISA 39.04\n03/15/26 01:21pm"
    record = run_receipt_parse(intake_id="intake-001", ocr_run_id="ocr-001", ocr_text=text)

    assert record.merchant_name == "Kroger"
    assert record.total == 39.04
    assert len(record.line_items) >= 2
