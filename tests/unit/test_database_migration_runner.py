from pathlib import Path

from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.database_migration_runner import run_migrations


def test_run_migrations(tmp_path: Path) -> None:
    connection = create_database_connection(tmp_path / "local_home_app.sqlite")
    try:
        run_migrations(connection)
        tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        assert len(tables) >= 4
    finally:
        connection.close()
