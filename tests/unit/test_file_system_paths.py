from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.config.application_settings import ApplicationSettings


def test_receipts_dir_path_suffix() -> None:
    paths = FileSystemPaths(ApplicationSettings())
    assert str(paths.receipts_dir()).endswith("receipts")
