"""Application settings for LocalHomeApp.

Purpose:
- Centralize typed configuration loading for runtime behavior.
- Separate portable application settings from machine-specific local values.

Inputs:
- Environment variables.

Outputs:
- Typed settings object used by application modules.

Dependencies:
- pydantic-settings

Execution context:
- Imported by CLI entry points and runtime modules.

Required permissions:
- Read access to local environment/config values.

Expected errors/failure modes:
- Missing required configuration.
- Invalid local path or OCR engine selection.

Related tests:
- tests/unit/test_application_settings.py

Related docs:
- docs/modules/application-settings.md
- docs/setup/development-setup.md
"""

from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationSettings(BaseSettings):
    """Typed application settings for LocalHomeApp."""

    model_config = SettingsConfigDict(
        env_prefix="LOCAL_HOME_APP_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    env_name: str = Field(default="development")
    data_root: str = Field(default="/Users/assistant/LocalHomeAppSensitiveData")
    database_path: str = Field(
        default="/Users/assistant/LocalHomeAppSensitiveData/database/local_home_app.sqlite"
    )
    telegram_bot_token: Optional[str] = Field(default=None)
    telegram_main_chat_id: str = Field(default="5143357049")
    telegram_workers_chat_id: str = Field(default="-5185231049")
    telegram_alerts_chat_id: str = Field(default="-5131828323")
    ocr_primary_engine: str = Field(default="apple_vision")
    ocr_fallback_engine: str = Field(default="tesseract")
    log_level: str = Field(default="INFO")
