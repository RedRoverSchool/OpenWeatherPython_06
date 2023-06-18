from pages.base_page import BasePage
from locators.locators import WeatherConditionsLocators


class WeatherConditionsPage(BasePage):


    def verify_count_of_icons_for_night_time(self, driver):
        icons = driver.find_elements(*WeatherConditionsLocators.ICONS_FOR_NIGHT_TIME)
        expected_minimum_icons_for_night_time = 8
        assert len(icons) >= expected_minimum_icons_for_night_time


    def check_codes_are_visible(self, driver, table):
        list_of_codes_each_table = driver.find_elements(*WeatherConditionsLocators.ELEMENTS_LOCATOR_CODES(table))
        for code in list_of_codes_each_table:
            assert code.is_displayed()


    def check_desc_are_visible(self, driver, table):
        list_of_desc_each_table = driver.find_elements(*WeatherConditionsLocators.ELEMENTS_LOCATOR_DESC(table))
        for desc in list_of_desc_each_table:
            assert desc.is_displayed()

    def check_visible_group_of_codes(self, group_locator):
        match group_locator:
            case 'clouds':
                clouds_codes = self.driver.find_element(*WeatherConditionsLocators.CLOUDS_LOCATOR)
                assert clouds_codes.is_displayed()
