"""Runtime error types for LocalHomeApp.

Purpose:
- Define explicit application-specific exceptions.

Inputs:
- n/a

Outputs:
- exception classes used by runtime modules

Dependencies:
- none

Execution context:
- imported throughout the application

Required permissions:
- none

Expected errors/failure modes:
- n/a

Related tests:
- tests/unit/test_runtime_errors.py

Related docs:
- docs/modules/runtime-errors.md
"""


class LocalHomeAppError(Exception):
    """Base application exception."""


class ConfigurationError(LocalHomeAppError):
    """Raised when application configuration is invalid."""


class TelegramIntegrationError(LocalHomeAppError):
    """Raised when Telegram integration fails."""


class OcrExecutionError(LocalHomeAppError):
    """Raised when local OCR execution fails."""
