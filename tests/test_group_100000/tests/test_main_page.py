from tests.test_group_100000.pages.main_page import *
from tests.test_group_100000.locators.main_page_locators import EightDayForecast as D8


def test_RF_TC_001_04_02_verify_state_of_sky_in_words_for_each_day_is_displayed(driver, open_and_load_main_page, wait):
    page = EightDayForecastPage(driver, link=D8.URL)
    page.open_page()
    page.verify_state_of_sky_in_words_for_each_day_is_displayed()
