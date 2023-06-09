from pages.base_page import BasePage
from locators.locators import WeatherConditionsLocators as locs

class WeatherConditionsPage(BasePage):

    def open_weather_conditions_page(self):
        self.driver.get(locs.WEATHER_CONDITIONS_PAGE_URL)


    def check_codes_are_visible(self, driver, table):
        list_of_codes_each_table = driver.find_elements(*locs.ELEMENTS_LOCATOR_CODES(table))
        print(list_of_codes_each_table[0].text)
        for code in list_of_codes_each_table:
            assert code.is_displayed()


    def check_desc_are_visible(self, driver, table):
        list_of_desc_each_table = driver.find_elements(*locs.ELEMENTS_LOCATOR_DESC(table))
        print(list_of_desc_each_table[0].text)
        for desc in list_of_desc_each_table:
            assert desc.is_displayed()
