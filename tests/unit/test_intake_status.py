from local_home_app.ingestion import intake_status


def test_intake_status_values_exist() -> None:
    assert intake_status.RECEIVED == "received"
    assert intake_status.DUPLICATE == "duplicate"
    assert intake_status.REJECTED == "rejected"
