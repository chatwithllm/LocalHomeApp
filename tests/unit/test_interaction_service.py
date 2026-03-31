import sqlite3

from local_home_app.query.interaction_service import InteractionService
from local_home_app.storage.purchase_history_repository import PurchaseHistoryRepository
from local_home_app.storage.storage_schema import create_storage_schema


def _seed(connection: sqlite3.Connection) -> None:
    connection.execute(
        "INSERT INTO receipt_parses (parse_id, intake_id, ocr_run_id, merchant_name, receipt_date, receipt_time, subtotal, tax, total, payment_method_summary, currency, parse_status, confidence_summary, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        ('parse-1', 'intake-1', 'ocr-1', 'Costco', '03/30/2026', '18:53', 460.13, 18.29, 478.42, 'VISA', 'USD', 'completed', 'medium', None),
    )
    connection.execute(
        "INSERT INTO receipt_line_items (line_id, parse_id, raw_text, item_name, quantity, unit_price, line_total, discount_text, confidence_summary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        ('line-1', 'parse-1', 'SPRING ROLL 9.99', 'SPRING ROLL', None, None, 9.99, None, 'medium'),
    )
    connection.execute(
        "INSERT INTO receipt_line_items (line_id, parse_id, raw_text, item_name, quantity, unit_price, line_total, discount_text, confidence_summary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        ('line-2', 'parse-1', 'MINI CUKES 4.89', 'MINI CUKES', None, None, 4.89, None, 'medium'),
    )
    connection.commit()


def test_interaction_service_recent_receipts() -> None:
    connection = sqlite3.connect(':memory:')
    connection.row_factory = sqlite3.Row
    create_storage_schema(connection)
    _seed(connection)

    service = InteractionService(PurchaseHistoryRepository(connection))
    summary = service.summarize_recent_receipts(limit=5)
    assert summary.title == 'Recent receipts'
    assert any('Costco' in line for line in summary.lines)


def test_interaction_service_item_history() -> None:
    connection = sqlite3.connect(':memory:')
    connection.row_factory = sqlite3.Row
    create_storage_schema(connection)
    _seed(connection)

    service = InteractionService(PurchaseHistoryRepository(connection))
    summary = service.summarize_item_history('cukes', limit=5)
    assert summary.title == 'Item history for cukes'
    assert any('MINI CUKES' in line for line in summary.lines)


def test_interaction_service_receipts_for_merchant() -> None:
    connection = sqlite3.connect(':memory:')
    connection.row_factory = sqlite3.Row
    create_storage_schema(connection)
    _seed(connection)

    service = InteractionService(PurchaseHistoryRepository(connection))
    summary = service.summarize_receipts_for_merchant('Costco', limit=5)
    assert summary.title == 'Recent receipts for Costco'
    assert any('478.42' in line for line in summary.lines)
