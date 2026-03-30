from local_home_app.ingestion.telegram_bot_client import TelegramBotClient


def test_telegram_bot_client_initialization() -> None:
    client = TelegramBotClient("token123")
    assert client.bot_token == "token123"
