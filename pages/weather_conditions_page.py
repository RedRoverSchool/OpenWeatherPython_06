from pages.base_page import BasePage
from locators.locators import WeatherConditionsLocators


class WeatherConditionsPage(BasePage):


    def verify_count_of_icons_for_night_time(self, driver):
        icons = driver.find_elements(*WeatherConditionsLocators.ICONS_FOR_NIGHT_TIME)
        expected_minimum_icons_for_night_time = 8
        assert len(icons) >= expected_minimum_icons_for_night_time


