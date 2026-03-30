from local_home_app.signals.inventory_signal_generator import generate_inventory_signals
from local_home_app.signals.signal_models import PurchasePatternSignal


def test_generate_inventory_signals() -> None:
    pattern_signals = [
        PurchasePatternSignal('MILK', 'Kroger', 3, '03/15/26', 7.0),
        PurchasePatternSignal('BREAD', 'Kroger', 1, '03/15/26', None),
    ]
    signals = generate_inventory_signals(pattern_signals)
    assert len(signals) == 1
    assert signals[0].item_name == 'MILK'
