from pathlib import Path

from local_home_app.config.application_settings import ApplicationSettings


def test_application_settings_reads_env_file(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "LOCAL_HOME_APP_TELEGRAM_BOT_TOKEN=test-token\n",
        encoding="utf-8",
    )

    settings = ApplicationSettings(_env_file=env_file)
    assert settings.telegram_bot_token == "test-token"
