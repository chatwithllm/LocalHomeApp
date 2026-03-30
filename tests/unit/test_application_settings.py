from local_home_app.config.application_settings import ApplicationSettings


def test_application_settings_defaults() -> None:
    settings = ApplicationSettings()
    assert settings.env_name == "development"
    assert settings.telegram_main_chat_id == "5143357049"
