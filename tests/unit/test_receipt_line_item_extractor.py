from local_home_app.parsing.receipt_line_item_extractor import extract_line_items


def test_extract_line_items_filters_summary_lines() -> None:
    text = "MILK 3.99\nVISA 39.04\nTOTAL SAVINGS 1.70\nBREAD 2.49"
    items = extract_line_items(parse_id="parse-001", ocr_text=text)

    names = [item.item_name for item in items]
    assert "MILK" in names
    assert "BREAD" in names
    assert all("VISA" not in (name or "") for name in names)


def test_extract_line_items_captures_line_total_when_present() -> None:
    text = "MILK 3.99"
    items = extract_line_items(parse_id="parse-001", ocr_text=text)
    assert items[0].line_total == 3.99
    assert items[0].confidence_summary == "medium"


def test_extract_line_items_filters_amount_only_and_store_boilerplate() -> None:
    text = "39.04\nWAL*MART\nST# 1371 OP# 7273 TE# 1 TR# 459\nTIC TAC 4.47"
    items = extract_line_items(parse_id="parse-001", ocr_text=text)
    names = [item.item_name for item in items]
    assert names == ["TIC TAC"]


def test_extract_line_items_filters_city_state_lines() -> None:
    text = "COLUMBUS, IN\nTIC TAC 4.47"
    items = extract_line_items(parse_id="parse-001", ocr_text=text)
    names = [item.item_name for item in items]
    assert names == ["TIC TAC"]


def test_extract_line_items_filters_customer_and_sales_metadata() -> None:
    text = "Customer: JOHN DOE\nSales ID: A. PERSON\nGIMBAL 149.99"
    items = extract_line_items(parse_id="parse-001", ocr_text=text)
    names = [item.item_name for item in items]
    assert names == ["GIMBAL"]


def test_extract_line_items_supports_comma_decimal_amounts() -> None:
    text = "GIMBAL 149,99"
    items = extract_line_items(parse_id="parse-001", ocr_text=text)
    assert items[0].line_total == 149.99
    assert items[0].item_name == "GIMBAL"


def test_extract_line_items_costco_style_codes() -> None:
    text = "E 337754 SPRING ROLL 9.99 N\n1957747 BUFFALO TOP 44.97 Y"
    items = extract_line_items(parse_id="parse-001", ocr_text=text)

    assert len(items) == 2
    assert items[0].item_name == "SPRING ROLL"
    assert items[0].line_total == 9.99
    assert items[1].item_name == "BUFFALO TOP"
    assert items[1].line_total == 44.97


def test_extract_line_items_filters_costco_discount_and_member_noise() -> None:
    text = "111950970348\n377963 /1957747 9.00-\nMember\nE 720650 MINI CUKES 4.89 N"
    items = extract_line_items(parse_id="parse-001", ocr_text=text)

    assert len(items) == 1
    assert items[0].item_name == "MINI CUKES"
    assert items[0].line_total == 4.89
