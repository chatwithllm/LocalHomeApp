"""Print a simple purchase history summary from LocalHomeApp SQLite storage."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.purchase_history_repository import PurchaseHistoryRepository


def main() -> None:
    database_path = Path('/Users/assistant/LocalHomeAppSensitiveData/database/local_home_app.sqlite')
    connection = create_database_connection(database_path)
    try:
        rows = PurchaseHistoryRepository(connection).summarize_recent_receipts()
        print(f'database={database_path}')
        print(f'receipt_count={len(rows)}')
        for row in rows[:20]:
            print(
                f"merchant={row['merchant_name']} date={row['receipt_date']} total={row['total']} line_items={row['line_item_count']}"
            )
    finally:
        connection.close()


if __name__ == '__main__':
    main()
