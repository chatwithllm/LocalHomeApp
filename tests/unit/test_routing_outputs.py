from local_home_app.ingestion.intake_event_store import IntakeEventRecord
from local_home_app.ingestion.intake_result import RuntimeIntakeResult
from local_home_app.ingestion.routing_outputs import build_routing_outputs


def test_build_routing_outputs_for_success() -> None:
    result = RuntimeIntakeResult(
        record=IntakeEventRecord(
            intake_id="intake-001",
            source_channel="telegram",
            source_account_id="default",
            telegram_chat_id="5143357049",
            telegram_message_id="477",
            telegram_user_id="5143357049",
            telegram_file_id="abc123",
            telegram_file_unique_id="unique123",
            stored_at_path="/tmp/receipt.jpg",
            media_type="photo",
            mime_type="image/jpeg",
            file_size_bytes=1024,
            sha256="hash123",
            intake_status="received",
        ),
        worker_message="worker update",
        alert_message=None,
        stored_file_path=None,
    )

    outputs = build_routing_outputs(result)
    assert outputs.main_message is not None
    assert outputs.worker_message == "worker update"
    assert outputs.alert_message is None
