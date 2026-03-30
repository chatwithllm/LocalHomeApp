from pathlib import Path

from local_home_app.ocr.ocr_comparison_runner import run_ocr_comparison
from local_home_app.ocr.ocr_engine_interface import OcrEngineInterface
from local_home_app.ocr.ocr_result_models import OcrResultRecord


class FakeOcrEngine(OcrEngineInterface):
    def __init__(self, engine_name: str) -> None:
        self.engine_name = engine_name

    def run_ocr(self, *, intake_id: str, source_artifact_path: Path) -> OcrResultRecord:
        return OcrResultRecord(
            ocr_run_id=f"ocr-{self.engine_name}",
            intake_id=intake_id,
            engine_name=self.engine_name,
            engine_version=None,
            source_artifact_path=str(source_artifact_path),
            preprocessed_artifact_path=None,
            ocr_text=f"text-{self.engine_name}",
            confidence_summary=None,
            runtime_ms=1,
            status="completed",
        )


def test_run_ocr_comparison() -> None:
    comparison = run_ocr_comparison(
        intake_id="intake-001",
        source_artifact_path=Path("/tmp/receipt.jpg"),
        variants=[("raw", FakeOcrEngine("raw-engine")), ("prep", FakeOcrEngine("prep-engine"))],
    )

    assert len(comparison.entries) == 2
    assert comparison.entries[0].label == "raw"
    assert comparison.entries[1].result.engine_name == "prep-engine"
