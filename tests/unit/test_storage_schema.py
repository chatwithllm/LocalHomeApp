from pathlib import Path

from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.storage_schema import create_storage_schema


def test_create_storage_schema(tmp_path: Path) -> None:
    connection = create_database_connection(tmp_path / "local_home_app.sqlite")
    try:
        create_storage_schema(connection)
        tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        table_names = {row['name'] for row in tables}
        assert 'receipt_intake_events' in table_names
        assert 'ocr_results' in table_names
        assert 'receipt_parses' in table_names
        assert 'receipt_line_items' in table_names
    finally:
        connection.close()
