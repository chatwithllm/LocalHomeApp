from pathlib import Path

from local_home_app.ocr.ocr_engine_interface import OcrEngineInterface
from local_home_app.ocr.ocr_result_models import OcrResultRecord


class FakeOcrEngine(OcrEngineInterface):
    def run_ocr(self, *, intake_id: str, source_artifact_path: Path) -> OcrResultRecord:
        return OcrResultRecord(
            ocr_run_id="ocr-001",
            intake_id=intake_id,
            engine_name="fake",
            engine_version=None,
            source_artifact_path=str(source_artifact_path),
            preprocessed_artifact_path=None,
            ocr_text="text",
            confidence_summary=None,
            runtime_ms=1,
            status="completed",
        )


def test_fake_ocr_engine_implements_interface() -> None:
    engine = FakeOcrEngine()
    result = engine.run_ocr(intake_id="intake-001", source_artifact_path=Path("/tmp/a.jpg"))
    assert result.engine_name == "fake"
