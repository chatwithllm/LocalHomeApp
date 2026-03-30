"""Intake status constants for LocalHomeApp.

Purpose:
- Centralize intake status values used during Phase 1.

Inputs:
- n/a

Outputs:
- named status constants

Dependencies:
- none

Execution context:
- used throughout the intake workflow

Required permissions:
- none

Expected errors/failure modes:
- n/a

Related tests:
- tests/unit/test_intake_status.py

Related docs:
- docs/modules/intake-status.md
- docs/phases/phase-01-telegram-intake.md
"""

RECEIVED = "received"
DUPLICATE = "duplicate"
REJECTED = "rejected"
FAILED_DOWNLOAD = "failed_download"
STORED = "stored"
