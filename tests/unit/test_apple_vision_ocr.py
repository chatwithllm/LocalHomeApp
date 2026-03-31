from pathlib import Path

from local_home_app.ocr.apple_vision_ocr import AppleVisionOcrEngine


def test_apple_vision_ocr_returns_structured_result() -> None:
    engine = AppleVisionOcrEngine()
    result = engine.run_ocr(intake_id="intake-001", source_artifact_path=Path("/tmp/a.jpg"))
    assert result.engine_name == "apple_vision"
    assert result.status in {"completed", "not_available"}
    if result.status == "completed":
        assert isinstance(result.ocr_text, str)
    else:
        assert result.error_message is not None
