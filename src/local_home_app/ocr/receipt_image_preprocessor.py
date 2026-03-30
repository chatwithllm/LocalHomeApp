"""Receipt image preprocessing for LocalHomeApp.

Purpose:
- Improve OCR readiness for receipt artifacts before engine execution.

Inputs:
- local source artifact path
- optional destination directory for preprocessed artifacts

Outputs:
- preprocessed artifact path or passthrough source path

Dependencies:
- pathlib
- PIL (Pillow)

Execution context:
- used before OCR execution when preprocessing is beneficial.

Required permissions:
- read/write access to local OCR artifact storage

Expected errors/failure modes:
- unsupported image format
- preprocessing runtime failure

Related tests:
- tests/unit/test_receipt_image_preprocessor.py

Related docs:
- docs/modules/receipt-image-preprocessor.md
- docs/phases/phase-02-dual-local-ocr.md
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from PIL import Image, ImageOps


def prepare_receipt_image_for_ocr(
    source_artifact_path: Path,
    destination_dir: Optional[Path] = None,
) -> Path:
    """Create a basic OCR-friendly grayscale, autocontrasted image copy."""

    if source_artifact_path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
        return source_artifact_path

    if destination_dir is None:
        destination_dir = source_artifact_path.parent
    destination_dir.mkdir(parents=True, exist_ok=True)

    output_path = destination_dir / f"{source_artifact_path.stem}_preprocessed.png"

    with Image.open(source_artifact_path) as image:
        grayscale = ImageOps.grayscale(image)
        enhanced = ImageOps.autocontrast(grayscale)
        enhanced.save(output_path, format="PNG")

    return output_path
