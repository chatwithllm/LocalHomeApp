from pathlib import Path
import sqlite3


def test_sqlite_database_is_queryable(tmp_path: Path) -> None:
    database_path = tmp_path / 'local_home_app.sqlite'
    connection = sqlite3.connect(database_path)
    try:
        connection.execute('SELECT 1')
    finally:
        connection.close()

    reopened = sqlite3.connect(database_path)
    try:
        value = reopened.execute('SELECT 1').fetchone()[0]
        assert value == 1
    finally:
        reopened.close()
