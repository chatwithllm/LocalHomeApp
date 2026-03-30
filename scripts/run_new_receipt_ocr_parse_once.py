"""Run OCR and parsing once for the newest inbound receipt image."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.ocr.ocr_result_store import OcrResultStore
from local_home_app.ocr.tesseract_ocr import TesseractOcrEngine
from local_home_app.parsing.receipt_parse_runtime_service import run_receipt_parse
from local_home_app.parsing.receipt_parse_store import ReceiptParseStore


def main() -> None:
    inbound_dir = Path('/Users/assistant/.openclaw/media/inbound')
    candidates = sorted(inbound_dir.glob('*'), key=lambda p: p.stat().st_mtime, reverse=True)
    source_artifact_path = next(p for p in candidates if p.suffix.lower() in {'.jpg', '.jpeg', '.png', '.webp'})

    ocr_result = TesseractOcrEngine(
        preprocess=True,
        preprocessed_output_dir=Path('/Users/assistant/LocalHomeAppSensitiveData/ocr_outputs/preprocessed'),
    ).run_ocr(
        intake_id='manual-phase-03-new-receipt',
        source_artifact_path=source_artifact_path,
    )

    OcrResultStore(Path('/Users/assistant/LocalHomeAppSensitiveData/ocr_outputs/ocr_results.jsonl')).append(ocr_result)

    parse_result = run_receipt_parse(
        intake_id='manual-phase-03-new-receipt',
        ocr_run_id=ocr_result.ocr_run_id,
        ocr_text=ocr_result.ocr_text,
    )

    ReceiptParseStore(Path('/Users/assistant/LocalHomeAppSensitiveData/structured_outputs/receipt_parses.jsonl')).append(parse_result)

    print(f'source={source_artifact_path.name}')
    print(f'ocr_status={ocr_result.status}')
    print(f'ocr_runtime_ms={ocr_result.runtime_ms}')
    print(f'parse_id={parse_result.parse_id}')
    print(f'merchant={parse_result.merchant_name}')
    print(f'total={parse_result.total}')
    print(f'date={parse_result.receipt_date}')
    print(f'time={parse_result.receipt_time}')
    print(f'status={parse_result.parse_status}')
    print(f'confidence={parse_result.confidence_summary}')
    print(f'notes={parse_result.notes}')
    print(f'line_item_count={len(parse_result.line_items)}')
    print('ocr_text_start')
    print(ocr_result.ocr_text[:2500])
    print('ocr_text_end')
    print('line_items_start')
    for item in parse_result.line_items[:15]:
        print(f"item={item.item_name!r} total={item.line_total} confidence={item.confidence_summary}")
    print('line_items_end')


if __name__ == '__main__':
    main()
