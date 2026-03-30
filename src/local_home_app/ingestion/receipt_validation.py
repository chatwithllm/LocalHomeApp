"""Receipt payload validation for LocalHomeApp Phase 1.

Purpose:
- Validate whether an intake candidate is acceptable for receipt processing.

Inputs:
- Telegram receipt candidate

Outputs:
- Validation result describing acceptance or rejection

Dependencies:
- dataclasses

Execution context:
- Used before live intake processing writes local files.

Required permissions:
- None directly.

Expected errors/failure modes:
- Unsupported mime types
- Unsupported file extensions

Related tests:
- tests/unit/test_receipt_validation.py

Related docs:
- docs/modules/receipt-validation.md
- docs/phases/phase-01-telegram-intake.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


ALLOWED_MIME_TYPES = {
    "image/jpeg",
    "image/png",
    "application/pdf",
}
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "pdf"}


@dataclass(frozen=True)
class ReceiptValidationResult:
    accepted: bool
    reason: Optional[str] = None


def validate_receipt_candidate(candidate: TelegramReceiptCandidate) -> ReceiptValidationResult:
    """Validate a Telegram receipt candidate for allowed receipt-like formats."""

    if candidate.mime_type and candidate.mime_type not in ALLOWED_MIME_TYPES:
        return ReceiptValidationResult(
            accepted=False,
            reason=f"Unsupported mime type: {candidate.mime_type}",
        )

    if candidate.file_name and "." in candidate.file_name:
        extension = candidate.file_name.rsplit(".", 1)[-1].lower()
        if extension not in ALLOWED_EXTENSIONS:
            return ReceiptValidationResult(
                accepted=False,
                reason=f"Unsupported file extension: {extension}",
            )

    return ReceiptValidationResult(accepted=True)
