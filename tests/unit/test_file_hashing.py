from pathlib import Path

from local_home_app.ingestion.file_hashing import compute_sha256


def test_compute_sha256(tmp_path: Path) -> None:
    sample = tmp_path / "sample.txt"
    sample.write_text("receipt-data", encoding="utf-8")

    digest = compute_sha256(sample)
    assert len(digest) == 64
