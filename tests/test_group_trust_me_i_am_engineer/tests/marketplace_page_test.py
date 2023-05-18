from tests.test_group_trust_me_i_am_engineer.pages.marketplace_page import MarketplacePage
import pytest

def test_TC_007_02_01_verify_the_method_of_input_location(driver):
    page = MarketplacePage(driver)
    page.verify_the_method_of_input_location()

def test_TC_007_02_02_verify_search_by_location_name(driver):
    page = MarketplacePage(driver)
    page.verify_search_by_location_name()