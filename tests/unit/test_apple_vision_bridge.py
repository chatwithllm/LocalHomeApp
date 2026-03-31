from pathlib import Path

from local_home_app.ocr.apple_vision_bridge import AppleVisionBridgeResult, run_apple_vision_bridge


def test_apple_vision_bridge_returns_failure_or_text() -> None:
    result = run_apple_vision_bridge(Path("/tmp/a.jpg"))
    assert isinstance(result, AppleVisionBridgeResult)
    if result.success:
        assert isinstance(result.ocr_text, str)
    else:
        assert result.error_message is not None
