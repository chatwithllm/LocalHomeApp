from local_home_app.signals.signal_models import InventorySignal, PriceExpectationSignal, PurchasePatternSignal


def test_signal_models_fields() -> None:
    pattern = PurchasePatternSignal('MILK', 'Kroger', 3, '03/15/26', 7.0)
    price = PriceExpectationSignal('MILK', 'Kroger', 3.49, 2.99, 3.99, 3.99)
    inventory = InventorySignal('MILK', 'Kroger', 'repeat_purchase_pattern', 'Observed 3 purchases', 'low')

    assert pattern.item_name == 'MILK'
    assert price.average_price == 3.49
    assert inventory.signal_type == 'repeat_purchase_pattern'
