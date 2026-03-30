"""Telegram media download path planning for LocalHomeApp.

Purpose:
- Determine where downloaded Telegram receipt artifacts should be stored locally.

Inputs:
- Normalized Telegram receipt candidate.
- Filesystem path helper.

Outputs:
- Planned local artifact path.

Dependencies:
- pathlib
- telegram_receipt_ingest
- file_system_paths

Execution context:
- Used by intake service before and during media download.

Required permissions:
- Write access to local sensitive storage root.

Expected errors/failure modes:
- Missing file extension information.
- Uncreatable target directories.

Related tests:
- tests/unit/test_telegram_media_download.py

Related docs:
- docs/modules/telegram-media-download.md
- docs/architecture/data-flow.md
"""

from __future__ import annotations

from pathlib import Path

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


def build_local_receipt_artifact_path(
    candidate: TelegramReceiptCandidate, paths: FileSystemPaths
) -> Path:
    """Build the target local artifact path for a Telegram receipt."""

    extension = _resolve_extension(candidate)
    directory = paths.receipts_dir() / "raw" / "telegram"
    directory.mkdir(parents=True, exist_ok=True)
    filename = (
        f"telegram_{candidate.chat_id}_{candidate.message_id}_{candidate.file_id}.{extension}"
    )
    return directory / filename


def _resolve_extension(candidate: TelegramReceiptCandidate) -> str:
    if candidate.file_name and "." in candidate.file_name:
        return candidate.file_name.rsplit(".", 1)[-1].lower()

    if candidate.mime_type == "image/jpeg":
        return "jpg"
    if candidate.mime_type == "image/png":
        return "png"
    if candidate.mime_type == "application/pdf":
        return "pdf"

    return "bin"
