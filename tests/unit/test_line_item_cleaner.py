from local_home_app.quality.line_item_cleaner import clean_line_item_name


def test_clean_line_item_name_removes_trailing_codes() -> None:
    assert clean_line_item_name('TIC TAC 000980000781 F') == 'TIC TAC'


def test_clean_line_item_name_handles_empty() -> None:
    assert clean_line_item_name('   ') is None
