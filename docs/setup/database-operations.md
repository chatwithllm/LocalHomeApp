# Database Operations

## Purpose
Describe how LocalHomeApp currently initializes and validates the SQLite storage layer.

## Current storage system of record direction
LocalHomeApp is moving from phase-local JSONL persistence toward SQLite as the durable local storage layer for:
- receipt intake events
- OCR results
- structured parse results
- purchase history queries

## Current validation path
A controlled storage demo can:
1. create the local database
2. apply schema migrations
3. insert a receipt intake record
4. insert an OCR result
5. insert a structured parse result
6. query purchase history rows back from SQLite

## Current local demo commands
```bash
. .venv/bin/activate
python scripts/run_storage_persistence_demo.py
```

```bash
. .venv/bin/activate
python scripts/run_purchase_history_summary.py
```

## Current known limitation
Earlier phase JSONL stores still exist as transitional persistence paths. Phase 4 is gradually moving runtime usage toward SQLite-backed repositories.
