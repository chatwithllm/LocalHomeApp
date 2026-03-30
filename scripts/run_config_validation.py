"""Validate core LocalHomeApp runtime configuration."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from local_home_app.config.application_settings import ApplicationSettings


def main() -> None:
    settings = ApplicationSettings()

    print(f"env_name={settings.env_name}")
    print(f"data_root={settings.data_root}")
    print(f"database_path={settings.database_path}")
    print(f"telegram_main_chat_id={settings.telegram_main_chat_id}")
    print(f"telegram_workers_chat_id={settings.telegram_workers_chat_id}")
    print(f"telegram_alerts_chat_id={settings.telegram_alerts_chat_id}")
    print(f"ocr_primary_engine={settings.ocr_primary_engine}")
    print(f"ocr_fallback_engine={settings.ocr_fallback_engine}")
    print(f"telegram_token_present={'yes' if settings.telegram_bot_token else 'no'}")

    problems = []
    if not settings.data_root:
        problems.append('missing_data_root')
    if not settings.database_path:
        problems.append('missing_database_path')

    if problems:
        print('validation=fail')
        print('problems=' + ','.join(problems))
    else:
        print('validation=ok')


if __name__ == '__main__':
    main()
