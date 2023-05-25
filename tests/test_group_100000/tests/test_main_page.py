from tests.test_group_100000.pages.main_page import FooterBlock
from tests.test_group_100000.pages.main_page import *
from tests.test_group_100000.locators.main_page_locators import EightDayForecast as D8

class TestHowToStartLink:
    def test_TC_003_05_03_verify_how_to_start_link_is_clickable(self, driver):
        page = FooterBlock(driver, link='https://openweathermap.org/')
        page.open_page()
        page.verify_how_to_start_link_is_clickable()


class TestEightDayForecastPage:
    def test_RF_AT_001_04_02_verify_state_of_sky_in_words_for_each_day_is_displayed(self, driver, open_and_load_main_page, wait):
        page = EightDayForecastPage(driver, link=D8.URL)
        page.open_page()
        page.verify_state_of_sky_in_words_for_each_day_is_displayed()
