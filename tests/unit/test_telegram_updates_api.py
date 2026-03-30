from local_home_app.ingestion.telegram_updates_api import TelegramUpdatesApi


def test_telegram_updates_api_initialization() -> None:
    api = TelegramUpdatesApi("token123")
    assert api.bot_token == "token123"
