"""Filesystem path helpers for LocalHomeApp.

Purpose:
- Resolve local sensitive storage paths in a single place.
- Keep path logic explicit and portable.

Inputs:
- Application settings.

Outputs:
- Path helper methods for runtime modules.

Dependencies:
- pathlib

Execution context:
- Used by intake, OCR, parsing, storage, and export workflows.

Required permissions:
- Read/write access to configured local sensitive storage root.

Expected errors/failure modes:
- Invalid configured root path.
- Uncreatable directories.

Related tests:
- tests/unit/test_file_system_paths.py

Related docs:
- docs/modules/file-system-paths.md
- docs/architecture/privacy-boundaries.md
"""

from __future__ import annotations

from pathlib import Path

from local_home_app.config.application_settings import ApplicationSettings


class FileSystemPaths:
    """Resolve filesystem locations for LocalHomeApp."""

    def __init__(self, settings: ApplicationSettings) -> None:
        self.settings = settings
        self.data_root = Path(settings.data_root)

    def receipts_dir(self) -> Path:
        return self.data_root / "receipts"

    def ocr_outputs_dir(self) -> Path:
        return self.data_root / "ocr_outputs"

    def structured_outputs_dir(self) -> Path:
        return self.data_root / "structured_outputs"

    def database_path(self) -> Path:
        return Path(self.settings.database_path)

    def ensure_runtime_directories(self) -> None:
        for path in [
            self.receipts_dir(),
            self.ocr_outputs_dir(),
            self.structured_outputs_dir(),
            self.database_path().parent,
        ]:
            path.mkdir(parents=True, exist_ok=True)
