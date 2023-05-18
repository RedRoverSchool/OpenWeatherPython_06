import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import MarketplacePageLocators

class MarketplacePage(BasePage):
    URL_MARKETPLACE = 'https://home.openweathermap.org/marketplace'
    locators = MarketplacePageLocators()

    def verify_the_method_of_input_location(self):
        expected_method_list = ['By location', 'By coordinates', 'Import']
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()
        self.driver.find_element(*self.locators.HISTORY_BULK_SEARCH_LOCATION).click()
        methods = self.driver.find_elements(*self.locators.BUTTON_SEARCH_METHODS)
        actual_method_list = [el.text for el in methods]
        assert expected_method_list == actual_method_list, \
            "The actual list of methods does not match the expected list of methods"

    def verify_search_by_location_name(self):
        expected_location = "Malta"
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()
        search_loc = self.driver.find_element(*self.locators.HISTORY_BULK_SEARCH_LOCATION)

        self.element_is_clickable(self.locators.MAP_BUTTON_LOC)
        search_loc.click()
        self.driver.find_element(*self.locators.BUTTON_BY_LOCATION).click()
        search_loc.click()
        search_loc.send_keys(expected_location + Keys.ARROW_DOWN)

        self.element_is_clickable(self.locators.FIRST_SEARCH_ITEMS).click()
        actual_search_result = self.element_is_visible(self.locators.SEARCH_POP_UP_HEADER)
        assert expected_location == actual_search_result.text

    def verify_search_by_coordinates(self):
        expected_latitude = "55.755826"
        expected_longitude = "37.61173"
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()
        self.driver.find_element(*self.locators.HISTORY_BULK_SEARCH_LOCATION).click()
        self.driver.find_element(*self.locators.BUTTON_BY_COORDINATES).click()
        latitude = self.driver.find_element(*self.locators.INPUT_LATITUDE)
        latitude.send_keys(expected_latitude)
        longitude = self.driver.find_element(*self.locators.INPUT_LONGITUDE)
        longitude.send_keys(expected_longitude)
        longitude.send_keys(Keys.RETURN)
        actual_latitude = self.driver.find_element(*self.locators.LATITUDE_ON_MAP)
        actual_longitude = self.driver.find_element(*self.locators.LONGITUDE_ON_MAP)
        assert expected_latitude in actual_latitude.text and expected_longitude in actual_longitude.text