"""Run a controlled LocalHomeApp inventory signal demo from SQLite purchase history."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

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
        lines = format_recommendations(inventory_signals, price_signals)

        print(f'database={database_path}')
        print(f'purchase_rows={len(rows)}')
        print(f'usable_rows={len(usable_rows)}')
        print(f'skipped={dict(skipped)}')
        print(f'pattern_signals={len(pattern_signals)}')
        print(f'price_signals={len(price_signals)}')
        print(f'inventory_signals={len(inventory_signals)}')
        for line in lines[:20]:
            print(line)
    finally:
        connection.close()


if __name__ == '__main__':
    main()
