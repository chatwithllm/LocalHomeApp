from pathlib import Path

from PIL import Image

from local_home_app.ocr.receipt_image_preprocessor import prepare_receipt_image_for_ocr


def test_prepare_receipt_image_for_ocr_creates_preprocessed_copy(tmp_path: Path) -> None:
    source = tmp_path / "receipt.jpg"
    Image.new("RGB", (20, 20), color="white").save(source)

    output = prepare_receipt_image_for_ocr(source, destination_dir=tmp_path / "preprocessed")

    assert output != source
    assert output.exists()
    assert output.suffix == ".png"


def test_prepare_receipt_image_for_ocr_passthrough_for_pdf(tmp_path: Path) -> None:
    source = tmp_path / "receipt.pdf"
    source.write_bytes(b"%PDF-test")

    output = prepare_receipt_image_for_ocr(source)
    assert output == source
