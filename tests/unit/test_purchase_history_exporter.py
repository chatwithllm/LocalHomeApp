from local_home_app.output.purchase_history_exporter import export_purchase_history_json


def test_export_purchase_history_json() -> None:
    payload = export_purchase_history_json([
        {'merchant_name': 'Kroger', 'item_name': 'MILK', 'line_total': 3.99}
    ])
    assert 'Kroger' in payload
    assert 'MILK' in payload
