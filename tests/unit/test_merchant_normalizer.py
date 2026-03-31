from local_home_app.quality.merchant_normalizer import normalize_merchant_name


def test_normalize_merchant_name_variants() -> None:
    assert normalize_merchant_name('wal*mart supercenter') == 'Walmart'
    assert normalize_merchant_name('icro Center') == 'Micro Center'
    assert normalize_merchant_name('METLJER SAVINGS') == 'Meijer'
