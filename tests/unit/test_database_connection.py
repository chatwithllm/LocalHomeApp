from pathlib import Path

from local_home_app.storage.database_connection import create_database_connection


def test_create_database_connection(tmp_path: Path) -> None:
    connection = create_database_connection(tmp_path / "local_home_app.sqlite")
    try:
        assert connection is not None
    finally:
        connection.close()
