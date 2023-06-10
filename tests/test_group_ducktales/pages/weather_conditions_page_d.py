from pages.base_page import BasePage
from ..locators.weather_conditions_locators_d import WeatherConditionsLocators as locs


class WeatherConditionsPage(BasePage):

    def open_weather_conditions_page(self):
        self.driver.get(locs.WEATHER_CONDITIONS_PAGE_URL)


    def check_codes_are_visible(self, driver, table):
        list_of_codes_each_table = driver.find_elements(*locs.ELEMENTS_LOCATOR_CODES(table))
        for code in list_of_codes_each_table:
            assert code.is_displayed()


    def check_desc_are_visible(self, driver, table):
        list_of_desc_each_table = driver.find_elements(*locs.ELEMENTS_LOCATOR_DESC(table))
        for desc in list_of_desc_each_table:
            assert desc.is_displayed()
