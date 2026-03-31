from local_home_app.parsing.receipt_header_extractor import extract_receipt_header


def test_extract_receipt_header_basic_fields() -> None:
    text = "KROGER\nVISA 39.04\n03/15/26 01:21pm"
    record = extract_receipt_header(intake_id="intake-001", ocr_run_id="ocr-001", ocr_text=text)

    assert record.merchant_name == "Kroger"
    assert record.total == 39.04
    assert record.receipt_date == "03/15/26"


def test_extract_receipt_header_payment_total_fallback() -> None:
    text = "icro Center\nMASTERCARD: 684.77\n01/09/26 8:55 PM"
    record = extract_receipt_header(intake_id="intake-001", ocr_run_id="ocr-001", ocr_text=text)

    assert record.merchant_name == "Micro Center"
    assert record.total == 684.77


def test_extract_receipt_header_tolerates_spaced_decimal_amounts() -> None:
    text = "METLJER SAVINGS\nTOTAL 36 .54\n03/14/26 18:19"
    record = extract_receipt_header(intake_id="intake-001", ocr_run_id="ocr-001", ocr_text=text)

    assert record.merchant_name == "Meijer"
    assert record.total == 36.54


def test_extract_receipt_header_costco_fields() -> None:
    text = "COSTCO\nCASTLETON #346\n03-31-26 16:02\nTOTAL 287.48"
    record = extract_receipt_header(intake_id="intake-001", ocr_run_id="ocr-001", ocr_text=text)

    assert record.merchant_name == "Costco"
    assert record.receipt_date == "03-31-26"
    assert record.total == 287.48


def test_extract_receipt_header_costco_totals_block_and_long_date() -> None:
    text = "COSTCO\nSUBTOTAL\n460.13\nTAX\n18.29\nTOTAL\n478.42\n03/30/2026 18:53"
    record = extract_receipt_header(intake_id="intake-001", ocr_run_id="ocr-001", ocr_text=text)

    assert record.merchant_name == "Costco"
    assert record.subtotal == 460.13
    assert record.tax == 18.29
    assert record.total == 478.42
    assert record.receipt_date == "03/30/2026"
