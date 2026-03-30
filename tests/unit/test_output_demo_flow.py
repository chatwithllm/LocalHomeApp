from local_home_app.output.output_models import PurchaseHistorySummaryOutput, ReceiptSummaryOutput, SignalSummaryOutput
from local_home_app.output.output_runtime_service import build_outputs
from local_home_app.output.purchase_history_exporter import export_purchase_history_json
from local_home_app.signals.inventory_signal_generator import generate_inventory_signals
from local_home_app.signals.price_expectation_engine import build_price_expectations
from local_home_app.signals.purchase_pattern_analyzer import analyze_purchase_patterns
from local_home_app.signals.recommendation_formatter import format_recommendations
from local_home_app.signals.signal_input_filter import filter_signal_input_rows


def test_output_demo_flow() -> None:
    rows = [
        {'merchant_name': 'Kroger', 'receipt_date': '03/01/26', 'item_name': 'MILK', 'line_total': 3.99},
        {'merchant_name': 'Kroger', 'receipt_date': '03/08/26', 'item_name': 'MILK', 'line_total': 4.49},
    ]
    usable_rows, skipped = filter_signal_input_rows(rows)
    pattern_signals = analyze_purchase_patterns(usable_rows)
    price_signals = build_price_expectations(usable_rows)
    inventory_signals = generate_inventory_signals(pattern_signals)
    signal_lines = format_recommendations(inventory_signals, price_signals)

    outputs = build_outputs(
        receipt_summary=ReceiptSummaryOutput('Kroger', '03/08/26', None, 'stored_history_summary'),
        purchase_history_summary=PurchaseHistorySummaryOutput(2, ['Kroger']),
        signal_summary=SignalSummaryOutput(signal_lines),
    )

    export_json = export_purchase_history_json(usable_rows)

    assert skipped == {}
    assert 'Merchant: Kroger' in outputs.local_report
    assert 'Receipt: Kroger' in outputs.telegram_summary
    assert 'MILK' in export_json
