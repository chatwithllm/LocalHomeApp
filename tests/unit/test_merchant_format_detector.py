from local_home_app.parsing.merchant_format_detector import detect_merchant_name


def test_detect_merchant_name_costco() -> None:
    assert detect_merchant_name("COSTCO WHOLESALE") == "Costco"


def test_detect_merchant_name_kroger() -> None:
    assert detect_merchant_name("KROGER SAVINGS") == "Kroger"


def test_detect_merchant_name_walmart() -> None:
    assert detect_merchant_name("WAL*MART Save money. Live better.") == "Walmart"


def test_detect_merchant_name_micro_center() -> None:
    assert detect_merchant_name("icro Center") == "Micro Center"


def test_detect_merchant_name_meijer() -> None:
    assert detect_merchant_name("METLJER SAVINGS") == "Meijer"


def test_detect_merchant_name_unknown() -> None:
    assert detect_merchant_name("Random text") is None
