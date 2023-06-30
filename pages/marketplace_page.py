import os

from pages.base_page import BasePage
from locators.locators import MarketplaceLocators as M
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from test_data.all_links import Links


class MarketplacePage(BasePage):
    def select_state_field(self):
        self.element_is_clickable(M.SELECT_STATE_FIELD).click()

    def select_element_from_dropdown_list(self, locator):
        self.element_is_present(locator).click()

    def select_year_field(self):
        self.element_is_clickable(M.SELECT_YEAR_FIELD).click()

    def find_price_in_dropdown_menu(self, locator):
        submenu = self.element_is_present(locator)
        s = (submenu.text)
        price = s.split(' (')[0]
        return price

    def find_total_amount(self, locator):
        t = self.element_is_present(locator)
        total = t.text
        amount = total.split()[1]
        return f'${amount}'


    def click_marketplace_search_field(self):
        marketplace_search_field = self.driver.find_element(*M.SEARCH_FLD)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(marketplace_search_field)
        self.driver.execute_script("arguments[0].click();", marketplace_search_field)
        return marketplace_search_field

    def select_by_location_method(self):
        by_location_button = self.driver.find_element(*M.BY_LOCATION_BTN)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(by_location_button)
        self.driver.execute_script("arguments[0].click();", by_location_button)
        return by_location_button

    def fill_marketplace_search_field(self):
        input_city_name = self.driver.find_element(*M.SEARCH_FLD)
        input_city_name.click()
        input_city_name.send_keys("Paris")

    def select_city_from_dropdown_list(self, wait):
        wait.until(EC.visibility_of_element_located(M.CITY_NAME_FROM_DROPDOWN_MENU))
        city_name_from_dropdown_list = self.element_is_clickable(M.CITY_NAME_FROM_DROPDOWN_MENU)
        city_name_from_dropdown_list.click()
        return city_name_from_dropdown_list

    def find_displayed_text(self, wait):
        displayed_text = wait.until(EC.visibility_of_element_located(M.CITY_NAME_ON_MAP)).text
        return displayed_text
        requested_city = "Paris"
        assert displayed_text == requested_city, '\n======== WRONG CITY! ========\n'

    def verify_the_method_of_input_location(self):
        expected_method_list = ['By location', 'By coordinates', 'Import']
        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()
        self.driver.find_element(*M.SEARCH_FLD).click()
        methods = self.driver.find_elements(*M.BUTTON_SEARCH_METHODS)
        actual_method_list = [el.text for el in methods]
        assert expected_method_list == actual_method_list, \
            "The actual list of methods does not match the expected list of methods"

    def verify_search_by_coordinates(self):
        expected_latitude = "55.755826"
        expected_longitude = "37.61173"
        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()
        self.driver.find_element(*M.SEARCH_FLD).click()
        self.driver.find_element(*M.BUTTON_BY_COORDINATES).click()
        latitude = self.driver.find_element(*M.INPUT_LATITUDE)
        latitude.send_keys(expected_latitude)
        longitude = self.driver.find_element(*M.INPUT_LONGITUDE)
        longitude.send_keys(expected_longitude)
        longitude.send_keys(Keys.RETURN)
        actual_latitude = self.driver.find_element(*M.LATITUDE_ON_MAP)
        actual_longitude = self.driver.find_element(*M.LONGITUDE_ON_MAP)
        assert expected_latitude in actual_latitude.text and expected_longitude in actual_longitude.text

    def verify_visibility_clickability_map_btn(self):
        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()
        map_button = self.element_is_clickable(M.MAP_BUTTON_LOC)
        assert map_button.is_displayed() and map_button.is_enabled(), \
            "The 'Map' button is not displayed on the map or is not clickable"

    def verify_search_by_import_csv(self):
        csv_file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'test_data/test_search_by_import.csv'))
        with open(csv_file_path, 'r') as f:
            csv_str = f.readline()
        expected_location, expected_latitude, expected_longitude = csv_str.split(";")

        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()

        input_file = self.driver.find_element(*M.INPUT_FIELD_UPLOAD_FILE)
        div_input_file = self.driver.find_element(*M.DIV_FIELD_UPLOAD_FILE)

        self.driver.execute_script("arguments[0].setAttribute('class','visible')", input_file)
        self.driver.execute_script("arguments[0].setAttribute('class','visible')", div_input_file)

        input_file.send_keys(csv_file_path)
        actual_location = self.driver.find_element(*M.LOCATION_NAME_TABLE)
        actual_latitude = self.driver.find_element(*M.LATITUDE_TABLE)
        actual_longitude = self.driver.find_element(*M.LONGITUDE_TABLE)
        assert actual_location.text.strip() == expected_location \
               and actual_latitude.text.strip() == expected_latitude \
               and actual_longitude.text.strip() == expected_longitude

    def verify_visibility_clickability_satellite_btn(self):
        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()
        satellite_button = self.element_is_clickable(M.SATELLITE_BUTTON_LOC)
        assert satellite_button.is_displayed() and satellite_button.is_enabled(), \
            "The 'Satellite' button is not displayed on the map or is not clickable"

    def verify_visibility_clickability_terrain_checkbox(self):
        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()
        self.element_is_clickable(M.MAP_BUTTON_LOC).click()
        terrain_checkbox = self.element_is_clickable(M.CHECKBOX_TERRAIN)
        assert terrain_checkbox.is_displayed() and terrain_checkbox.is_enabled(), \
            "The 'Terrain' checkbox is not displayed on the map or is not clickable"

    def verify_visibility_clickability_zoom_out(self):
        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()
        zoom_out_btn = self.element_is_clickable(M.BUTTON_ZOOM_OUT)
        assert zoom_out_btn.is_displayed() and zoom_out_btn.is_enabled(), \
            "The 'Zoom out' button is not displayed on the map or is not clickable"

    def verify_visibility_clickability_street_view_btn(self):
        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()
        street_view_btn = self.element_is_clickable(M.BUTTON_STREET_VIEW)
        assert street_view_btn.is_displayed() and street_view_btn.is_enabled(), \
            "The 'Street view' button is not displayed on the map or is not clickable"

    def verify_visibility_clickability_full_screen_btn(self):
        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()
        full_screen_btn = self.element_is_clickable(M.BUTTON_FULL_SCREEN)
        assert full_screen_btn.is_displayed() and full_screen_btn.is_enabled(), \
            "The 'Full screen' button is not displayed on the map or is not clickable"

    def verify_visibility_clickability_labels_checkbox(self):
        self.driver.get(Links.URL_MARKETPLACE)
        self.driver.find_element(*M.HISTORY_BULK_TITLE).click()
        self.element_is_clickable(M.SATELLITE_BUTTON_LOC).click()
        labels_checkbox = self.element_is_clickable(M.CHECKBOX_LABELS)
        assert labels_checkbox.is_displayed() and labels_checkbox.is_enabled(), \
            "The 'Terrain' checkbox is not displayed on the map or is not clickable"

    def verify_name_of_location_and_its_coordinates_were_added_to_the_order(self, wait):
        self.driver.find_element(*M.ADD_LOCATION_BTN).click()
        displayed_text = wait.until(EC.visibility_of_element_located(M.LST_NAME_CITY)).text
        displayed_latitude = wait.until(EC.visibility_of_element_located(M.LST_LATITUDE_COORDINATE)).text
        displayed_longitude = wait.until(EC.visibility_of_element_located(M.LST_LONGITUDE_COORDINATE)).text
        return displayed_text, displayed_latitude, displayed_longitude
        expected_city = "Paris"
        expected_latitude = "48.856614"
        expected_longitude = "2.352222"
        assert displayed_text == expected_city \
               and displayed_latitude == expected_latitude \
               and displayed_longitude == expected_longitude


    def find_feels_like_in_parameters(self):
        expected_parameter = "Feels like"
        feels_like = self.driver.find_element(*M.FEELS_LIKE_PARAMETER).text
        assert expected_parameter == feels_like, "Parameter Feels like is absent"

    def count_points_in_weather_parameters_list(self):
        title_weather_parameters = self.driver.find_element(*M.HEADER_WEATHER_PAR)
        expected_title = "Weather parameters"
        markers = self.driver.find_elements(*M.WEATHER_PAR_MARKERS)
        assert len(markers) == 11 and expected_title == title_weather_parameters.text


