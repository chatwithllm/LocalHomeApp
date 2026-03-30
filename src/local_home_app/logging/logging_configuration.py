"""Logging configuration for LocalHomeApp.

Purpose:
- Provide a centralized logging setup with privacy-aware defaults.

Inputs:
- Log level and runtime configuration.

Outputs:
- Configured Python logging behavior.

Dependencies:
- standard library logging

Execution context:
- Used by scripts and long-running workers.

Required permissions:
- Optional write access to local log destinations.

Expected errors/failure modes:
- Invalid log level configuration.
- Unwritable log destinations when file handlers are added.

Related tests:
- tests/unit/test_logging_configuration.py

Related docs:
- docs/modules/logging-configuration.md
- docs/standards/coding-standards.md
"""

from __future__ import annotations

import logging


def configure_logging(log_level: str = "INFO") -> None:
    """Configure root logging for LocalHomeApp."""

    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        force=True,
    )
