import pytest
from tests.test_group_100000.pages.marketplace_page import *
from tests.test_group_100000.locators.marketplace_page_locators import MarketplaceLocators as M


def test_RF_TC_007_01_01_Select_state_from_dropdown_list(driver):
    page = MarketplacePage(driver, link=M.URL_HISTORICAL_WEATHER)
    page.open_page()
    page.select_state_field()
    expected_state = "Texas"
    selected_state = driver.find_element(*M.STATE_TEXAS).text
    assert expected_state == selected_state, '\n======== WRONG STATE! ========\n'

