"""Run a controlled LocalHomeApp output demo from SQLite data."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.output.output_models import (
    PurchaseHistorySummaryOutput,
    ReceiptSummaryOutput,
    SignalSummaryOutput,
)
from local_home_app.output.output_runtime_service import build_outputs
from local_home_app.output.purchase_history_exporter import export_purchase_history_json
from local_home_app.signals.inventory_signal_generator import generate_inventory_signals
from local_home_app.signals.price_expectation_engine import build_price_expectations
from local_home_app.signals.purchase_pattern_analyzer import analyze_purchase_patterns
from local_home_app.signals.recommendation_formatter import format_recommendations
from local_home_app.signals.signal_input_filter import filter_signal_input_rows
from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.purchase_history_repository import PurchaseHistoryRepository


def main() -> None:
    database_path = Path('/Users/assistant/LocalHomeAppSensitiveData/database/local_home_app.sqlite')
    connection = create_database_connection(database_path)
    try:
        rows = [dict(row) for row in PurchaseHistoryRepository(connection).list_line_items()]
        usable_rows, skipped = filter_signal_input_rows(rows)
        pattern_signals = analyze_purchase_patterns(usable_rows)
        price_signals = build_price_expectations(usable_rows)
        inventory_signals = generate_inventory_signals(pattern_signals)
        signal_lines = format_recommendations(inventory_signals, price_signals)

        merchants = sorted({row.get('merchant_name') for row in rows if row.get('merchant_name')})
        latest = rows[-1] if rows else {}

        outputs = build_outputs(
            receipt_summary=ReceiptSummaryOutput(
                merchant_name=latest.get('merchant_name'),
                receipt_date=latest.get('receipt_date'),
                total=None,
                parse_status='stored_history_summary',
            ),
            purchase_history_summary=PurchaseHistorySummaryOutput(
                receipt_count=len(rows),
                merchants=merchants,
            ),
            signal_summary=SignalSummaryOutput(signal_lines),
        )

        export_json = export_purchase_history_json(usable_rows[:10])

        print(f'database={database_path}')
        print(f'purchase_rows={len(rows)}')
        print(f'usable_rows={len(usable_rows)}')
        print(f'skipped={dict(skipped)}')
        print('local_report_start')
        print(outputs.local_report)
        print('local_report_end')
        print('telegram_summary_start')
        print(outputs.telegram_summary)
        print('telegram_summary_end')
        print('json_export_start')
        print(export_json[:2000])
        print('json_export_end')
    finally:
        connection.close()


if __name__ == '__main__':
    main()
