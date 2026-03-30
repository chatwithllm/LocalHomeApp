from pathlib import Path

from local_home_app.parsing.receipt_parse_runtime_service import run_receipt_parse
from local_home_app.parsing.receipt_parse_store import ReceiptParseStore


def test_run_receipt_parse_and_store_real_fixture(tmp_path: Path) -> None:
    fixture_path = Path("tests/fixtures/kroger_ocr_sample.txt")
    text = fixture_path.read_text(encoding="utf-8")

    record = run_receipt_parse(
        intake_id="fixture-intake-001",
        ocr_run_id="fixture-ocr-001",
        ocr_text=text,
    )

    store = ReceiptParseStore(tmp_path / "receipt_parses.jsonl")
    store.append(record)
    loaded = store.load_all()

    assert len(loaded) == 1
    assert loaded[0].merchant_name == "Kroger"
    assert loaded[0].total == 39.04
