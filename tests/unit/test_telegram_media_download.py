from local_home_app.common.file_system_paths import FileSystemPaths
from local_home_app.config.application_settings import ApplicationSettings
from local_home_app.ingestion.telegram_media_download import build_local_receipt_artifact_path
from local_home_app.ingestion.telegram_receipt_ingest import TelegramReceiptCandidate


def test_build_local_receipt_artifact_path_for_jpeg() -> None:
    paths = FileSystemPaths(ApplicationSettings())
    candidate = TelegramReceiptCandidate(
        chat_id="5143357049",
        message_id="477",
        user_id="5143357049",
        media_type="photo",
        file_id="abc123",
        file_unique_id="unique123",
        file_name=None,
        mime_type="image/jpeg",
        file_size_bytes=1024,
    )

    path = build_local_receipt_artifact_path(candidate, paths)
    assert path.name == "telegram_5143357049_477_abc123.jpg"
