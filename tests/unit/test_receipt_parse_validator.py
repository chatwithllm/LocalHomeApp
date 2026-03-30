from local_home_app.parsing.receipt_parse_models import ReceiptLineItemRecord, ReceiptParseRecord
from local_home_app.parsing.receipt_parse_validator import validate_receipt_parse


def test_validate_receipt_parse_completed_when_merchant_and_total_present() -> None:
    record = ReceiptParseRecord(
        parse_id="parse-001",
        intake_id="intake-001",
        ocr_run_id="ocr-001",
        merchant_name="Kroger",
        receipt_date=None,
        receipt_time=None,
        subtotal=None,
        tax=None,
        total=39.04,
        payment_method_summary=None,
        currency="USD",
        parse_status="partial",
        confidence_summary=None,
        notes=None,
        line_items=[
            ReceiptLineItemRecord(
                line_id="line-001",
                parse_id="parse-001",
                raw_text="MILK 3.99",
                item_name="MILK",
                quantity=None,
                unit_price=None,
                line_total=3.99,
                discount_text=None,
                confidence_summary="medium",
            )
        ],
    )

    validated = validate_receipt_parse(record)
    assert validated.parse_status == "completed"
    assert validated.confidence_summary == "medium"
