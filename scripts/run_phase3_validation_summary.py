"""Run a 3-sample parsing validation summary for LocalHomeApp Phase 3."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.ocr.tesseract_ocr import TesseractOcrEngine
from local_home_app.parsing.receipt_parse_runtime_service import run_receipt_parse


def summarize(label: str, ocr_text: str) -> None:
    parse = run_receipt_parse(
        intake_id=f"summary-{label}",
        ocr_run_id=f"ocr-{label}",
        ocr_text=ocr_text,
    )
    print(f"sample={label}")
    print(f"merchant={parse.merchant_name}")
    print(f"total={parse.total}")
    print(f"date={parse.receipt_date}")
    print(f"time={parse.receipt_time}")
    print(f"status={parse.parse_status}")
    print(f"confidence={parse.confidence_summary}")
    print(f"notes={parse.notes}")
    print(f"line_item_count={len(parse.line_items)}")
    for item in parse.line_items[:8]:
        print(f"item={item.item_name!r} total={item.line_total} confidence={item.confidence_summary}")
    print("---")


def main() -> None:
    kroger_text = Path("tests/fixtures/kroger_ocr_sample.txt").read_text(encoding="utf-8")
    summarize("kroger_fixture", kroger_text)

    walmart_source = Path("/Users/assistant/.openclaw/media/inbound/3dd8b4be-ad57-4044-9c88-41d857da0376.png")
    walmart_ocr = TesseractOcrEngine(
        preprocess=True,
        preprocessed_output_dir=Path('/Users/assistant/LocalHomeAppSensitiveData/ocr_outputs/preprocessed'),
    ).run_ocr(
        intake_id="summary-walmart",
        source_artifact_path=walmart_source,
    )
    summarize("walmart_receipt", walmart_ocr.ocr_text)

    micro_source = Path("/Users/assistant/.openclaw/media/inbound/1531d6a4-5531-41b8-91f8-c4ca7503ced6.jpg")
    micro_ocr = TesseractOcrEngine(
        preprocess=True,
        preprocessed_output_dir=Path('/Users/assistant/LocalHomeAppSensitiveData/ocr_outputs/preprocessed'),
    ).run_ocr(
        intake_id="summary-micro-center",
        source_artifact_path=micro_source,
    )
    summarize("micro_center_receipt", micro_ocr.ocr_text)


if __name__ == '__main__':
    main()
