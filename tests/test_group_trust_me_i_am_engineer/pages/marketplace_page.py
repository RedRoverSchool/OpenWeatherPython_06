import os
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

    def verify_visibility_clickability_map_btn(self):
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()
        map_button = self.element_is_clickable(self.locators.MAP_BUTTON_LOC)
        assert map_button.is_displayed() and map_button.is_enabled(), \
            "The 'Map' button is not displayed on the map or is not clickable"

    def verify_search_by_import_csv(self):
        csv_file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'test_data/search_by_import.csv'))
        with open(csv_file_path, 'r') as f:
            csv_str = f.readline()
        expected_location, expected_latitude, expected_longitude = csv_str.split(";")

        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()

        input_file = self.driver.find_element(*self.locators.INPUT_FIELD_UPLOAD_FILE)
        div_input_file = self.driver.find_element(*self.locators.DIV_FIELD_UPLOAD_FILE)

        self.driver.execute_script("arguments[0].setAttribute('class','visible')", input_file)
        self.driver.execute_script("arguments[0].setAttribute('class','visible')", div_input_file)

        input_file.send_keys(csv_file_path)
        actual_location = self.driver.find_element(*self.locators.LOCATION_NAME_TABLE)
        actual_latitude = self.driver.find_element(*self.locators.LATITUDE_TABLE)
        actual_longitude = self.driver.find_element(*self.locators.LONGITUDE_TABLE)
        assert actual_location.text.strip() == expected_location \
               and actual_latitude.text.strip() == expected_latitude \
               and actual_longitude.text.strip() == expected_longitude

    def verify_visibility_clickability_satellite_btn(self):
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()
        satellite_button = self.element_is_clickable(self.locators.SATELLITE_BUTTON_LOC)
        assert satellite_button.is_displayed() and satellite_button.is_enabled(), \
            "The 'Satellite' button is not displayed on the map or is not clickable"

    def verify_visibility_clickability_terrain_checkbox(self):
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()
        self.element_is_clickable(self.locators.MAP_BUTTON_LOC).click()
        terrain_checkbox = self.element_is_clickable(self.locators.CHECKBOX_TERRAIN)
        assert terrain_checkbox.is_displayed() and terrain_checkbox.is_enabled(), \
            "The 'Terrain' checkbox is not displayed on the map or is not clickable"

    def verify_visibility_clickability_zoom_in(self, wait):
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()
        self.element_is_displayed(self.locators.BUTTON_ZOOM_IN, wait)
        self.element_is_visible(self.locators.BUTTON_ZOOM_IN).click()
        assert self.element_is_visible(self.locators.BUTTON_ZOOM_IN) and self.element_is_clickable(self.locators.BUTTON_ZOOM_IN)

    def verify_visibility_clickability_zoom_out(self):
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()
        zoom_out_btn = self.element_is_clickable(self.locators.BUTTON_ZOOM_OUT)
        assert zoom_out_btn.is_displayed() and zoom_out_btn.is_enabled(), \
            "The 'Zoom out' button is not displayed on the map or is not clickable"

    def verify_visibility_clickability_street_view_btn(self):
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BULK_TITLE).click()
        street_view_btn = self.element_is_clickable(self.locators.BUTTON_STREET_VIEW)
        assert street_view_btn.is_displayed() and street_view_btn.is_enabled(), \
            "The 'Zoom out' button is not displayed on the map or is not clickable"