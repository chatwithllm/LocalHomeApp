from pathlib import Path

from local_home_app.ocr.apple_vision_ocr import AppleVisionOcrEngine


def test_apple_vision_ocr_returns_not_available_until_bridge_exists() -> None:
    engine = AppleVisionOcrEngine()
    result = engine.run_ocr(intake_id="intake-001", source_artifact_path=Path("/tmp/a.jpg"))
    assert result.engine_name == "apple_vision"
    assert result.status == "not_available"
    assert result.error_message is not None
