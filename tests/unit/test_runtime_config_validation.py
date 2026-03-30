from pathlib import Path

from local_home_app.config.application_settings import ApplicationSettings


def test_application_settings_has_required_runtime_fields(tmp_path: Path) -> None:
    env_file = tmp_path / '.env'
    env_file.write_text(
        '\n'.join([
            'LOCAL_HOME_APP_DATA_ROOT=/tmp/data',
            'LOCAL_HOME_APP_DATABASE_PATH=/tmp/data/local_home_app.sqlite',
        ]),
        encoding='utf-8',
    )
    settings = ApplicationSettings(_env_file=env_file)
    assert settings.data_root == '/tmp/data'
    assert settings.database_path == '/tmp/data/local_home_app.sqlite'
