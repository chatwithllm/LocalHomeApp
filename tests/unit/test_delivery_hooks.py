from local_home_app.ingestion.delivery_hooks import build_delivery_payloads
from local_home_app.ingestion.routing_outputs import IntakeRoutingOutputs


def test_build_delivery_payloads() -> None:
    outputs = IntakeRoutingOutputs(
        main_message="main ok",
        worker_message="worker ok",
        alert_message="alert ok",
    )

    payloads = build_delivery_payloads(outputs)
    assert len(payloads) == 3
    assert payloads[0].target == "main"
    assert payloads[1].target == "workers"
    assert payloads[2].target == "alerts"
