from local_home_app.quality.quality_scoring import score_item_quality


def test_score_item_quality_usable() -> None:
    assert score_item_quality(merchant_name='Kroger', item_name='MILK', line_total=3.99) == 'usable'


def test_score_item_quality_weak() -> None:
    assert score_item_quality(merchant_name=None, item_name=None, line_total=None) == 'weak'
