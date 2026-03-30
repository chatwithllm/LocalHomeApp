from local_home_app.signals.price_expectation_engine import build_price_expectations


def test_build_price_expectations() -> None:
    rows = [
        {'merchant_name': 'Kroger', 'item_name': 'MILK', 'line_total': 3.99},
        {'merchant_name': 'Kroger', 'item_name': 'MILK', 'line_total': 2.99},
        {'merchant_name': 'Kroger', 'item_name': 'MILK', 'line_total': 3.49},
    ]
    signals = build_price_expectations(rows)
    assert len(signals) == 1
    assert round(signals[0].average_price, 2) == 3.49
    assert signals[0].max_price == 3.99
