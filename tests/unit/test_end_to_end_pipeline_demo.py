from pathlib import Path

from local_home_app.output.output_models import PurchaseHistorySummaryOutput, ReceiptSummaryOutput, SignalSummaryOutput
from local_home_app.output.output_runtime_service import build_outputs
from local_home_app.parsing.receipt_parse_runtime_service import run_receipt_parse
from local_home_app.signals.inventory_signal_generator import generate_inventory_signals
from local_home_app.signals.price_expectation_engine import build_price_expectations
from local_home_app.signals.purchase_pattern_analyzer import analyze_purchase_patterns
from local_home_app.signals.recommendation_formatter import format_recommendations
from local_home_app.signals.signal_input_filter import filter_signal_input_rows


def test_end_to_end_pipeline_demo_flow() -> None:
    fixture_text = Path('tests/fixtures/kroger_ocr_sample.txt').read_text(encoding='utf-8')
    parse = run_receipt_parse(
        intake_id='demo-intake',
        ocr_run_id='demo-ocr',
        ocr_text=fixture_text,
    )
    rows = [
        {
            'merchant_name': parse.merchant_name,
            'receipt_date': parse.receipt_date,
            'item_name': item.item_name,
            'line_total': item.line_total,
        }
        for item in parse.line_items
    ]
    usable_rows, skipped = filter_signal_input_rows(rows)
    pattern_signals = analyze_purchase_patterns(usable_rows)
    price_signals = build_price_expectations(usable_rows)
    inventory_signals = generate_inventory_signals(pattern_signals)
    signal_lines = format_recommendations(inventory_signals, price_signals)
    output = build_outputs(
        receipt_summary=ReceiptSummaryOutput(parse.merchant_name, parse.receipt_date, parse.total, parse.parse_status),
        purchase_history_summary=PurchaseHistorySummaryOutput(1, [parse.merchant_name] if parse.merchant_name else []),
        signal_summary=SignalSummaryOutput(signal_lines),
    )
    assert output.local_report
    assert output.telegram_summary
    assert isinstance(skipped, dict)
