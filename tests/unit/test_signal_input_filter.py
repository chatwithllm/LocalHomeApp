from local_home_app.signals.signal_input_filter import filter_signal_input_rows


def test_filter_signal_input_rows() -> None:
    rows = [
        {'merchant_name': 'Kroger', 'item_name': 'MILK', 'line_total': 3.99},
        {'merchant_name': 'Kroger', 'item_name': 'TOTAL SAVINGS', 'line_total': None},
        {'merchant_name': 'Kroger', 'item_name': 'AB', 'line_total': 1.0},
        {'merchant_name': 'wal*mart supercenter', 'item_name': 'TIC TAC 000980000781 F', 'line_total': 4.47},
        {'merchant_name': 'Kroger', 'item_name': 'BREAD', 'line_total': 2.49},
    ]

    usable, skipped = filter_signal_input_rows(rows)
    assert len(usable) == 3

    walmart_row = next(row for row in usable if row['merchant_name'] == 'Walmart')
    assert walmart_row['item_name'] == 'TIC TAC'
    assert walmart_row['quality_label'] == 'usable'
    assert skipped['missing_price'] == 1
    assert skipped['too_short'] == 1
