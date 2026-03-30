"""Storage schema definition for LocalHomeApp.

Purpose:
- Define the initial SQLite schema for LocalHomeApp storage.

Inputs:
- sqlite3 connection

Outputs:
- created schema tables and indexes

Dependencies:
- sqlite3

Execution context:
- used by migration and setup workflows.

Required permissions:
- write access to local database

Expected errors/failure modes:
- schema creation failure

Related tests:
- tests/unit/test_storage_schema.py

Related docs:
- docs/modules/storage-schema.md
- docs/phases/phase-04-local-storage.md
"""

from __future__ import annotations

import sqlite3


SCHEMA_STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS receipt_intake_events (
        intake_id TEXT PRIMARY KEY,
        source_channel TEXT NOT NULL,
        source_account_id TEXT NOT NULL,
        telegram_chat_id TEXT,
        telegram_message_id TEXT,
        telegram_user_id TEXT,
        telegram_file_id TEXT,
        telegram_file_unique_id TEXT,
        stored_at_path TEXT NOT NULL,
        media_type TEXT NOT NULL,
        mime_type TEXT,
        file_size_bytes INTEGER,
        sha256 TEXT,
        intake_status TEXT NOT NULL,
        duplicate_of_intake_id TEXT,
        notes TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS ocr_results (
        ocr_run_id TEXT PRIMARY KEY,
        intake_id TEXT NOT NULL,
        engine_name TEXT NOT NULL,
        engine_version TEXT,
        source_artifact_path TEXT NOT NULL,
        preprocessed_artifact_path TEXT,
        ocr_text TEXT NOT NULL,
        confidence_summary TEXT,
        runtime_ms INTEGER,
        status TEXT NOT NULL,
        error_message TEXT,
        FOREIGN KEY(intake_id) REFERENCES receipt_intake_events(intake_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS receipt_parses (
        parse_id TEXT PRIMARY KEY,
        intake_id TEXT NOT NULL,
        ocr_run_id TEXT NOT NULL,
        merchant_name TEXT,
        receipt_date TEXT,
        receipt_time TEXT,
        subtotal REAL,
        tax REAL,
        total REAL,
        payment_method_summary TEXT,
        currency TEXT,
        parse_status TEXT NOT NULL,
        confidence_summary TEXT,
        notes TEXT,
        FOREIGN KEY(intake_id) REFERENCES receipt_intake_events(intake_id),
        FOREIGN KEY(ocr_run_id) REFERENCES ocr_results(ocr_run_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS receipt_line_items (
        line_id TEXT PRIMARY KEY,
        parse_id TEXT NOT NULL,
        raw_text TEXT NOT NULL,
        item_name TEXT,
        quantity REAL,
        unit_price REAL,
        line_total REAL,
        discount_text TEXT,
        confidence_summary TEXT,
        FOREIGN KEY(parse_id) REFERENCES receipt_parses(parse_id)
    )
    """,
]


def create_storage_schema(connection: sqlite3.Connection) -> None:
    for statement in SCHEMA_STATEMENTS:
        connection.execute(statement)
    connection.commit()
