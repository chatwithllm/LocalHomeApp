from typing import Optional

from local_home_app.ocr.ocr_comparison_models import OcrComparisonEntry, OcrComparisonRecord
from local_home_app.ocr.ocr_evaluation_summary import render_ocr_evaluation_summary, summarize_ocr_comparison
from local_home_app.ocr.ocr_result_models import OcrResultRecord


def _result(label: str, status: str, text: str, runtime_ms: Optional[int] = 10) -> OcrResultRecord:
    return OcrResultRecord(
        ocr_run_id=f'run-{label}',
        intake_id='intake-1',
        engine_name=label,
        engine_version=None,
        source_artifact_path='/tmp/test.png',
        preprocessed_artifact_path=None,
        ocr_text=text,
        confidence_summary=None,
        runtime_ms=runtime_ms,
        status=status,
        error_message=None if status == 'completed' else 'failed',
    )


def test_summarize_ocr_comparison() -> None:
    record = OcrComparisonRecord(
        comparison_id='cmp-1',
        intake_id='intake-1',
        entries=[
            OcrComparisonEntry(label='apple_vision', result=_result('apple_vision', 'completed', 'KROGER\nTOTAL 6.48')),
            OcrComparisonEntry(label='tesseract', result=_result('tesseract', 'failed', '')),
        ],
    )

    summary = summarize_ocr_comparison(record)
    assert summary.completed_labels == ['apple_vision']
    assert summary.failed_labels == ['tesseract']
    assert summary.entries[0].line_count == 2


def test_render_ocr_evaluation_summary() -> None:
    record = OcrComparisonRecord(
        comparison_id='cmp-1',
        intake_id='intake-1',
        entries=[OcrComparisonEntry(label='apple_vision', result=_result('apple_vision', 'completed', 'KROGER\nTOTAL 6.48'))],
    )
    summary = summarize_ocr_comparison(record)
    rendered = render_ocr_evaluation_summary(summary)
    assert 'OCR comparison: intake-1' in rendered
    assert 'apple_vision' in rendered
    assert 'preview: KROGER' in rendered
