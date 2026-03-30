from pathlib import Path

from PIL import Image

from local_home_app.ocr.tesseract_ocr import TesseractOcrEngine


def test_tesseract_ocr_returns_not_available_when_binary_missing(tmp_path: Path) -> None:
    source = tmp_path / "a.jpg"
    Image.new("RGB", (20, 20), color="white").save(source)

    engine = TesseractOcrEngine(binary_name="definitely-not-a-real-tesseract-binary")
    result = engine.run_ocr(intake_id="intake-001", source_artifact_path=source)
    assert result.engine_name == "tesseract"
    assert result.status == "not_available"


def test_tesseract_ocr_preprocesses_image_when_enabled(tmp_path: Path) -> None:
    source = tmp_path / "receipt.jpg"
    Image.new("RGB", (20, 20), color="white").save(source)

    engine = TesseractOcrEngine(
        binary_name="definitely-not-a-real-tesseract-binary",
        preprocess=True,
        preprocessed_output_dir=tmp_path / "preprocessed",
    )
    result = engine.run_ocr(intake_id="intake-001", source_artifact_path=source)

    assert result.status == "not_available"
    assert result.preprocessed_artifact_path is not None
    assert Path(result.preprocessed_artifact_path).exists()
