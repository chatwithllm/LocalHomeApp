from local_home_app.ingestion.telegram_update_handler import extract_receipt_candidate_from_update


def test_extract_receipt_candidate_from_photo_update() -> None:
    candidate = extract_receipt_candidate_from_update(
        {
            "message": {
                "message_id": 477,
                "chat": {"id": 5143357049},
                "from": {"id": 5143357049},
                "photo": [
                    {"file_id": "small", "file_unique_id": "u1", "file_size": 100},
                    {"file_id": "large", "file_unique_id": "u2", "file_size": 200},
                ],
            }
        }
    )

    assert candidate is not None
    assert candidate.file_id == "large"
    assert candidate.media_type == "photo"


def test_extract_receipt_candidate_from_non_media_update_returns_none() -> None:
    candidate = extract_receipt_candidate_from_update(
        {
            "message": {
                "message_id": 478,
                "chat": {"id": 5143357049},
                "from": {"id": 5143357049},
                "text": "hello",
            }
        }
    )

    assert candidate is None
