from tests.test_group_100000.pages.api_page import *
from tests.test_group_100000.locators.api_page_locators import WeatherConditions as W


class TestWeatherConditions:
    def test_RF_AT_001_12_04_Drizzle_group_of_codes_visible(self, driver):
        page = WeatherConditionsPage(driver, link=W.CONDITION_URL)
        page.open_page()
        page.check_visibility_drizzle_group()


