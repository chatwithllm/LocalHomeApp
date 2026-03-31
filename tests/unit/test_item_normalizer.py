from local_home_app.quality.item_normalizer import normalize_item_name


def test_normalize_item_name_uppercases() -> None:
    assert normalize_item_name('Tic Tac') == 'TIC TAC'
