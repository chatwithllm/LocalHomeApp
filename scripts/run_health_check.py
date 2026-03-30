"""Run a simple LocalHomeApp health check."""

from pathlib import Path
import sqlite3
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.config.application_settings import ApplicationSettings


def main() -> None:
    settings = ApplicationSettings()
    checks = []

    data_root = Path(settings.data_root)
    checks.append(("data_root_exists", data_root.exists()))

    database_path = Path(settings.database_path)
    checks.append(("database_exists", database_path.exists()))

    db_ok = False
    if database_path.exists():
        try:
            connection = sqlite3.connect(database_path)
            connection.execute('SELECT 1')
            connection.close()
            db_ok = True
        except sqlite3.Error:
            db_ok = False
    checks.append(("database_query_ok", db_ok))

    token_present = bool(settings.telegram_bot_token)
    checks.append(("telegram_token_present", token_present))

    for name, ok in checks:
        print(f"{name}={'ok' if ok else 'fail'}")


if __name__ == '__main__':
    main()
