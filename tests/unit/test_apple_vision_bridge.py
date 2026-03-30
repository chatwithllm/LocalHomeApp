from pathlib import Path

from local_home_app.ocr.apple_vision_bridge import run_apple_vision_bridge


def test_apple_vision_bridge_scaffold_returns_failure() -> None:
    result = run_apple_vision_bridge(Path("/tmp/a.jpg"))
    assert result.success is False
    assert result.error_message is not None
