from local_home_app.signals.recommendation_formatter import format_recommendations
from local_home_app.signals.signal_models import InventorySignal, PriceExpectationSignal


def test_format_recommendations() -> None:
    inventory = [
        InventorySignal('MILK', 'Kroger', 'repeat_purchase_pattern', 'Observed 3 purchases; average interval 7.0 days', 'low')
    ]
    prices = [
        PriceExpectationSignal('MILK', 'Kroger', 3.49, 2.99, 3.99, 3.99)
    ]
    lines = format_recommendations(inventory, prices)
    assert len(lines) == 2
    assert 'MILK' in lines[0]
