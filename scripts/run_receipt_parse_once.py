"""Run one controlled receipt parse test for LocalHomeApp Phase 3."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.parsing.receipt_parse_runtime_service import run_receipt_parse
from local_home_app.parsing.receipt_parse_store import ReceiptParseStore


def main() -> None:
    fixture_path = Path("tests/fixtures/kroger_ocr_sample.txt")
    ocr_text = fixture_path.read_text(encoding="utf-8")

    result = run_receipt_parse(
        intake_id="manual-phase-03-parse",
        ocr_run_id="fixture-ocr-001",
        ocr_text=ocr_text,
    )

    store = ReceiptParseStore(
        Path("/Users/assistant/LocalHomeAppSensitiveData/structured_outputs/receipt_parses.jsonl")
    )
    store.append(result)

    print(f"parse_id={result.parse_id}")
    print(f"merchant={result.merchant_name}")
    print(f"total={result.total}")
    print(f"status={result.parse_status}")
    print(f"confidence={result.confidence_summary}")
    print(f"notes={result.notes}")
    print(f"line_item_count={len(result.line_items)}")
    for item in result.line_items[:10]:
        print(f"item={item.item_name!r} total={item.line_total} confidence={item.confidence_summary}")


if __name__ == "__main__":
    main()
