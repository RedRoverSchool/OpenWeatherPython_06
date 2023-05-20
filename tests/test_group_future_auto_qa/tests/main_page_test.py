from tests.test_group_future_auto_qa.pages.main_page import *
import pytest


def test_tc_002_02_07_verify_placeholder_is_displayed_in_search_field(driver, open_and_load_main_page, wait):
    main_page = MainPage(driver)
    search_placeholder_text = main_page.get_header_search_field_attribute("placeholder")
    assert search_placeholder_text == "Weather in your city", \
        "Password field placeholder text is incorrect or missing"
