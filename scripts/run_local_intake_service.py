"""Local intake service entry point for LocalHomeApp.

Current state:
- initializes settings and logging
- runs a single polling pass for controlled Phase 1 testing
- prints delivery payloads generated from receipt-related Telegram updates
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.config.application_settings import ApplicationSettings
from local_home_app.ingestion.local_intake_store import LocalIntakeStore
from local_home_app.ingestion.polling_runtime_loop import process_polled_updates
from local_home_app.ingestion.telegram_bot_client import TelegramBotClient
from local_home_app.ingestion.telegram_updates_api import TelegramUpdatesApi
from local_home_app.logging.logging_configuration import configure_logging


def main() -> None:
    settings = ApplicationSettings()
    configure_logging(settings.log_level)

    paths = FileSystemPaths(settings)
    paths.ensure_runtime_directories()

    metadata_path = Path(settings.data_root) / "metadata" / "intake.jsonl"
    store = LocalIntakeStore(metadata_path)
    updates_api = TelegramUpdatesApi(settings.telegram_bot_token or "")
    bot_client = TelegramBotClient(settings.telegram_bot_token or "")

    result = process_polled_updates(
        updates_api=updates_api,
        paths=paths,
        store=store,
        bot_client=bot_client,
        offset=None,
        timeout=0,
    )

    print(f"Next offset: {result.next_offset}")
    for payload in result.delivery_payloads:
        print(f"[{payload.target}] {payload.message}")


if __name__ == "__main__":
    main()
