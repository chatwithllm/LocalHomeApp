from local_home_app.parsing.receipt_parse_models import ReceiptLineItemRecord, ReceiptParseRecord


def test_receipt_parse_record_fields() -> None:
    line = ReceiptLineItemRecord(
        line_id="line-001",
        parse_id="parse-001",
        raw_text="MILK 3.99",
        item_name="MILK",
        quantity=1,
        unit_price=3.99,
        line_total=3.99,
        discount_text=None,
        confidence_summary=None,
    )
    record = ReceiptParseRecord(
        parse_id="parse-001",
        intake_id="intake-001",
        ocr_run_id="ocr-001",
        merchant_name="Kroger",
        receipt_date="03/15/26",
        receipt_time="01:21pm",
        subtotal=None,
        tax=None,
        total=39.04,
        payment_method_summary="VISA",
        currency="USD",
        parse_status="partial",
        confidence_summary=None,
        notes=None,
        line_items=[line],
    )

    assert record.total == 39.04
    assert record.line_items[0].item_name == "MILK"
