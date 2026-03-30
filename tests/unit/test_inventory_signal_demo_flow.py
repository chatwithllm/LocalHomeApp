from pathlib import Path

from local_home_app.signals.inventory_signal_generator import generate_inventory_signals
from local_home_app.signals.price_expectation_engine import build_price_expectations
from local_home_app.signals.purchase_pattern_analyzer import analyze_purchase_patterns
from local_home_app.signals.recommendation_formatter import format_recommendations
from local_home_app.storage.database_connection import create_database_connection
from local_home_app.storage.database_migration_runner import run_migrations
from local_home_app.storage.purchase_history_repository import PurchaseHistoryRepository


def test_inventory_signal_demo_flow(tmp_path: Path) -> None:
    connection = create_database_connection(tmp_path / "local_home_app.sqlite")
    try:
        run_migrations(connection)
        connection.execute(
            "INSERT INTO receipt_intake_events (intake_id, source_channel, source_account_id, stored_at_path, media_type, intake_status) VALUES (?, ?, ?, ?, ?, ?)",
            ("intake-001", "telegram", "default", "/tmp/receipt.jpg", "photo", "received"),
        )
        connection.execute(
            "INSERT INTO ocr_results (ocr_run_id, intake_id, engine_name, source_artifact_path, ocr_text, status) VALUES (?, ?, ?, ?, ?, ?)",
            ("ocr-001", "intake-001", "tesseract", "/tmp/receipt.jpg", "TOTAL 3.99", "completed"),
        )
        connection.execute(
            "INSERT INTO receipt_parses (parse_id, intake_id, ocr_run_id, merchant_name, receipt_date, total, parse_status) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("parse-001", "intake-001", "ocr-001", "Kroger", "03/01/26", 3.99, "completed"),
        )
        connection.execute(
            "INSERT INTO receipt_line_items (line_id, parse_id, raw_text, item_name, line_total) VALUES (?, ?, ?, ?, ?)",
            ("line-001", "parse-001", "MILK 3.99", "MILK", 3.99),
        )
        connection.execute(
            "INSERT INTO receipt_intake_events (intake_id, source_channel, source_account_id, stored_at_path, media_type, intake_status) VALUES (?, ?, ?, ?, ?, ?)",
            ("intake-002", "telegram", "default", "/tmp/receipt2.jpg", "photo", "received"),
        )
        connection.execute(
            "INSERT INTO ocr_results (ocr_run_id, intake_id, engine_name, source_artifact_path, ocr_text, status) VALUES (?, ?, ?, ?, ?, ?)",
            ("ocr-002", "intake-002", "tesseract", "/tmp/receipt2.jpg", "TOTAL 4.49", "completed"),
        )
        connection.execute(
            "INSERT INTO receipt_parses (parse_id, intake_id, ocr_run_id, merchant_name, receipt_date, total, parse_status) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("parse-002", "intake-002", "ocr-002", "Kroger", "03/08/26", 4.49, "completed"),
        )
        connection.execute(
            "INSERT INTO receipt_line_items (line_id, parse_id, raw_text, item_name, line_total) VALUES (?, ?, ?, ?, ?)",
            ("line-002", "parse-002", "MILK 4.49", "MILK", 4.49),
        )
        connection.commit()

        rows = [dict(row) for row in PurchaseHistoryRepository(connection).list_line_items()]
        pattern_signals = analyze_purchase_patterns(rows)
        price_signals = build_price_expectations(rows)
        inventory_signals = generate_inventory_signals(pattern_signals)
        formatted = format_recommendations(inventory_signals, price_signals)

        assert len(pattern_signals) >= 1
        assert len(price_signals) >= 1
        assert len(inventory_signals) >= 1
        assert any('MILK' in line for line in formatted)
    finally:
        connection.close()
