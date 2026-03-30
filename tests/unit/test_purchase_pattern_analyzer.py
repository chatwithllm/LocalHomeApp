from local_home_app.signals.purchase_pattern_analyzer import analyze_purchase_patterns


def test_analyze_purchase_patterns() -> None:
    rows = [
        {'merchant_name': 'Kroger', 'item_name': 'MILK', 'receipt_date': '03/01/26'},
        {'merchant_name': 'Kroger', 'item_name': 'MILK', 'receipt_date': '03/08/26'},
        {'merchant_name': 'Kroger', 'item_name': 'MILK', 'receipt_date': '03/15/26'},
    ]
    signals = analyze_purchase_patterns(rows)
    assert len(signals) == 1
    assert signals[0].purchase_count == 3
    assert signals[0].average_days_between_purchases == 7.0
