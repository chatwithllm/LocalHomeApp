"""File hashing helpers for LocalHomeApp intake.

Purpose:
- Compute stable content hashes for downloaded receipt artifacts.

Inputs:
- Local file paths.

Outputs:
- Hex SHA-256 digest strings.

Dependencies:
- hashlib
- pathlib

Execution context:
- Used after local receipt files are downloaded.

Required permissions:
- Read access to locally stored receipt files.

Expected errors/failure modes:
- Missing file path.
- Unreadable file.

Related tests:
- tests/unit/test_file_hashing.py

Related docs:
- docs/modules/file-hashing.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

import hashlib
from pathlib import Path


def compute_sha256(file_path: Path) -> str:
    """Compute a SHA-256 digest for a local file."""

    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()
