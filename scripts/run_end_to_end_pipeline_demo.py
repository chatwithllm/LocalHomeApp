"""Run a simple end-to-end LocalHomeApp pipeline demo using fixture data."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.output.output_models import PurchaseHistorySummaryOutput, ReceiptSummaryOutput, SignalSummaryOutput
from local_home_app.output.output_runtime_service import build_outputs
from local_home_app.parsing.receipt_parse_runtime_service import run_receipt_parse
from local_home_app.signals.inventory_signal_generator import generate_inventory_signals
from local_home_app.signals.price_expectation_engine import build_price_expectations
from local_home_app.signals.purchase_pattern_analyzer import analyze_purchase_patterns
from local_home_app.signals.recommendation_formatter import format_recommendations
from local_home_app.signals.signal_input_filter import filter_signal_input_rows


def main() -> None:
    fixture_text = Path('tests/fixtures/kroger_ocr_sample.txt').read_text(encoding='utf-8')
    parse = run_receipt_parse(
        intake_id='phase-07-demo-intake',
        ocr_run_id='phase-07-demo-ocr',
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
        receipt_summary=ReceiptSummaryOutput(
            merchant_name=parse.merchant_name,
            receipt_date=parse.receipt_date,
            total=parse.total,
            parse_status=parse.parse_status,
        ),
        purchase_history_summary=PurchaseHistorySummaryOutput(
            receipt_count=1,
            merchants=[parse.merchant_name] if parse.merchant_name else [],
        ),
        signal_summary=SignalSummaryOutput(signal_lines),
    )

    print(f"merchant={parse.merchant_name}")
    print(f"total={parse.total}")
    print(f"parse_status={parse.parse_status}")
    print(f"usable_rows={len(usable_rows)}")
    print(f"skipped={dict(skipped)}")
    print('local_report_start')
    print(output.local_report)
    print('local_report_end')
    print('telegram_summary_start')
    print(output.telegram_summary)
    print('telegram_summary_end')


if __name__ == '__main__':
    main()
