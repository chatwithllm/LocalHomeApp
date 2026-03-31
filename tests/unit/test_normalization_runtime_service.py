from local_home_app.quality.normalization_runtime_service import normalize_record


def test_normalize_record() -> None:
    result = normalize_record(
        merchant_name='wal*mart supercenter',
        item_name='TIC TAC 000980000781 F',
        line_total=4.47,
    )
    assert result.merchant_name == 'Walmart'
    assert result.cleaned_item_name == 'TIC TAC'
    assert result.normalized_item_name == 'TIC TAC'
    assert result.quality_label == 'usable'
