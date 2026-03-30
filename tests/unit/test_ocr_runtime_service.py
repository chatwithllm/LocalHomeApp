from pathlib import Path

from local_home_app.ocr.ocr_engine_interface import OcrEngineInterface
from local_home_app.ocr.ocr_result_models import OcrResultRecord
from local_home_app.ocr.ocr_runtime_service import run_ocr_for_artifact


class FakeOcrEngine(OcrEngineInterface):
    def run_ocr(self, *, intake_id: str, source_artifact_path: Path) -> OcrResultRecord:
        return OcrResultRecord(
            ocr_run_id="ocr-001",
            intake_id=intake_id,
            engine_name="fake",
            engine_version=None,
            source_artifact_path=str(source_artifact_path),
            preprocessed_artifact_path=None,
            ocr_text="ocr text",
            confidence_summary=None,
            runtime_ms=5,
            status="completed",
        )


def test_run_ocr_for_artifact() -> None:
    result = run_ocr_for_artifact(
        engine=FakeOcrEngine(),
        intake_id="intake-001",
        source_artifact_path=Path("/tmp/receipt.jpg"),
    )
    assert result.ocr_text == "ocr text"
