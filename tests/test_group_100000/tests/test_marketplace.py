import pytest
from tests.test_group_100000.pages.marketplace_page import *
from tests.test_group_100000.locators.marketplace_page_locators import MarketplaceLocators as M


@pytest.mark.parametrize('locator', [M.STATE_TEXAS])
def test_RF_TC_007_01_01_Select_state_from_dropdown_list(driver, locator):
    page = MarketplacePage(driver, link=M.URL_HISTORICAL_WEATHER)
    page.open_page()
    page.select_state_field()
    page.select_element_from_dropdown_list(locator)
    expected_state = "Texas"
    selected_state = driver.find_element(*M.STATE_TEXAS).text
    assert expected_state == selected_state, '\n======== WRONG STATE! ========\n'


@pytest.mark.parametrize('locator', [M.YEAR_2019])
def test_RF_TC_007_01_02_Select_year_from_dropdown_list(driver, locator):
    page = MarketplacePage(driver, link=M.URL_HISTORICAL_WEATHER)
    page.open_page()
    page.select_year_field()
    page.select_element_from_dropdown_list(locator)
    expected_year = "2019"
    selected_year = driver.find_element(*M.EXPECTED_YEAR).text
    assert expected_year == selected_year, '\n======== WRONG YEAR! ========\n'

