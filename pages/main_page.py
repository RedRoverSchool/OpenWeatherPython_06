from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators
from test_data.all_links import Links

class MainPage(BasePage):
    locators = MainPageLocators()

    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*self.locators.SEARCH_CITY_FIELD)
        input_city.send_keys(city)

    def search_city(self, city):
        self.fill_city_search_field(city)
        self.driver.find_element(*self.locators.SEARCH_BUTTON).click()

    def check_seach_city_result(self, wait, city):
        self.click_search_button(city)
        expected_city = city
        expected_error_message = f'No results for {city}'
        if self.element_is_displayed(self.locators.NO_RESULTS_NOTIFICATION, wait):
            actual_error_message = wait.until(EC.visibility_of_element_located(self.locators.NO_RESULTS_NOTIFICATION))
            actual_error_message_text = actual_error_message.text
            assert actual_error_message_text == expected_error_message
        else:
            wait.until(EC.element_to_be_clickable(self.locators.SEARCH_DROPDOWN_OPTION)).click()
            wait.until(EC.text_to_be_present_in_element(self.locators.DISPLAYED_CITY, city))
            actual_city = self.driver.find_element(*self.locators.DISPLAYED_CITY).text
            assert expected_city in actual_city

    def go_to_about_us_page_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.allow_all_cookies()
        main_page.element_is_clickable(self.locators.ABOUT_US_BUTTON).click()

    def choose_1st_option(self, wait):
        wait.until(EC.element_to_be_clickable(self.locators.SEARCH_DROPDOWN_OPTION)).click()

    def switch_to_c_temp(self):
        self.driver.find_element(*self.locators.C_TEMP_LOCATOR).click()

    def check_8_lines_are_displayed(self):
        lines = self.driver.find_elements(*self.locators.LINE_IN_8_DAYS_FORECAST_LOCATOR)
        for line in lines:
            assert line.is_displayed()

    def check_historical_weather_data_link_is_visible(self):
        historical_weather_data_link = self.element_is_visible(self.locators.HISTORICAL_WEATHER_DATA_LINK)
        assert historical_weather_data_link.is_displayed(), "The Historical Weather Data link is not visible"

    def check_historical_weather_data_link_functionality(self):
        historical_weather_data_link = self.driver.find_element(*self.locators.HISTORICAL_WEATHER_DATA_LINK)
        self.go_to_element(historical_weather_data_link)
        historical_weather_data_link.click()
        assert '/api#history' in self.driver.current_url, \
            "The Historical Weather Data link leads to an incorrect page"

    def check_weather_dashboard_link_is_visible(self):
        weather_dashboard_link = self.element_is_visible(self.locators.WEATHER_DASHBOARD_LINK)
        assert weather_dashboard_link.is_displayed(), "The Weather Dashboard link is not visible"

    def check_weather_dashboard_link_is_clickable(self):
        self.driver.find_element(*self.locators.COOKIES).click()
        weather_dashboard_link = self.driver.find_element(*self.locators.WEATHER_DASHBOARD_LINK)
        assert weather_dashboard_link.is_enabled(), "The Weather dashboard link is not clickable"

    def check_weather_dashboard_link_functionality(self):
        weather_dashboard_link = self.driver.find_element(*self.locators.WEATHER_DASHBOARD_LINK)
        self.go_to_element(weather_dashboard_link)
        weather_dashboard_link.click()
        assert '/weather-dashboard' in self.driver.current_url, \
            "The Weather Dashboard link leads to an incorrect page"

    def check_weather_maps_link_functionality(self):
        weather_maps_link = self.driver.find_element(*self.locators.WEATHER_MAPS_LINK)
        self.go_to_element(weather_maps_link)
        weather_maps_link.click()
        assert '/api#maps' in self.driver.current_url, \
            "The Weather Maps link leads to an incorrect page"

    def check_our_technology_link_functionality(self):
        our_technology_link = self.driver.find_element(*self.locators.OUR_TECHNOLOGY_LINK)
        self.go_to_element(our_technology_link)
        our_technology_link.click()
        assert '/technology' in self.driver.current_url, \
            "The Our technology link leads to an incorrect page"

    def check_accuracy_and_quality_of_weather_data_link_functionality(self):
        accuracy_and_quality_of_weather_data_link = \
            self.driver.find_element(*self.locators.ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK)
        self.go_to_element(accuracy_and_quality_of_weather_data_link)
        accuracy_and_quality_of_weather_data_link.click()
        assert '/accuracy-and-quality' in self.driver.current_url, \
            "The Accuracy and quality of weather data link leads to an incorrect page"

    def check_connect_your_weather_station_link_functionality(self):
        connect_your_weather_station_link = self.driver.find_element(*self.locators.CONNECT_YOUR_WEATHER_STATION_LINK)
        self.go_to_element(connect_your_weather_station_link)
        connect_your_weather_station_link.click()
        assert '/stations' in self.driver.current_url, \
            "The Connect your weather station link leads to an incorrect page"

    def check_how_to_start_link_functionality(self):
        how_to_start_link = self.driver.find_element(*self.locators.HOW_TO_START_LINK)
        self.go_to_element(how_to_start_link)
        how_to_start_link.click()
        assert '/appid' in self.driver.current_url, \
            "The How to start link leads to an incorrect page"

    def check_subscribe_for_free_link_functionality(self):
        subscribe_for_free_link = self.driver.find_element(*self.locators.SUBSCRIBE_FOR_FREE_LINK)
        self.go_to_element(subscribe_for_free_link)
        subscribe_for_free_link.click()
        assert '/users/sign_up' in self.driver.current_url, \
            "The Subscribe for free link leads to an incorrect page"

    def check_openweather_for_business_link_functionality(self, expected_link):
        self.allow_all_cookies()
        blog_link = self.element_is_clickable(self.locators.OPENWEATHER_FOR_BUSINESS_LINK)
        link_href = blog_link.get_attribute('href')
        assert link_href == expected_link, "Incorrect link"

    def check_website_terms_and_conditions_link_visibility(self):
        website_terms_and_conditions_link = self.driver.find_element(*self.locators.WEBSITE_TERMS_AND_CONDITIONS_LINK)
        assert website_terms_and_conditions_link.is_displayed(), "The Website terms and conditions link is not visible"

    def check_about_us_link_is_visible(self):
        about_us_link = self.driver.find_element(*self.locators.ABOUT_US_LINK)
        assert about_us_link.is_displayed(), "The About us link is not visible"

    def check_product_collections_module_is_visible(self):
        product_collections_module = self.driver.find_element(*self.locators.PRODUCT_COLLECTIONS)
        assert product_collections_module.is_displayed(), \
            "The footer is not displayed or does not contain the expected text"

    def get_header_search_field_attribute(self, attribute):
        '''To retrieve the value of a specific attribute from Header Search field'''
        search_placeholder = self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD)
        return search_placeholder.get_attribute(attribute)

    def check_placeholder_text_is_visible(self, expected_value):
        '''To retrieve the value of a specific attribute from Header Search field'''
        search_placeholder_text = self.get_header_search_field_attribute("placeholder")
        assert search_placeholder_text == expected_value, \
            "Password field placeholder text is incorrect or missing"

    def click_header_search_field(self):
        self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD).click()

    def check_placeholder_disappears(self, symbol, attribute):
        search_placeholder_text = self.get_header_search_field_attribute("placeholder")
        self.click_header_search_field()
        self.fill_city_search_field(symbol)
        assert search_placeholder_text not in self.get_header_search_field_attribute(attribute), \
            "The placeholder text is still visible in the search field after typing a symbol"


    def check_current_and_forecast_apis_functionality(self):
        current_and_forecast_apis = self.driver.find_element(*self.locators.CURRENT_AND_FORECAST_APIS)
        self.go_to_element(current_and_forecast_apis)
        current_and_forecast_apis.click()
        assert '/api#current' in self.driver.current_url, \
            "The link 'current_and_forecast_apis' leads to incorrect page"


    def verify_clickability_current_and_forecast_apis(self):
        self.driver.find_element(*self.locators.COOKIES).click()
        current_and_forecast_apis = self.driver.find_element(*self.locators.CURRENT_AND_FORECAST_APIS)
        assert current_and_forecast_apis.is_displayed() and current_and_forecast_apis.is_enabled(), \
            "The 'current_and_forecast_apis' link is not displayed on the page or is not clickable"


    def verify_widgets_clickability(self):
        self.driver.find_element(*self.locators.COOKIES).click()
        widgets = self.driver.find_element(*self.locators.WIDGETS)
        assert widgets.is_displayed() and widgets.is_enabled(), \
            "The 'widgets' link is not displayed on the page or is not clickable"


    def verify_how_to_start_visibility(self):
        how_to_start = self.driver.find_element(*self.locators.HOW_TO_START)
        assert how_to_start.is_displayed(), "The How to start link is not visible"

    def verify_privacy_policy_is_opened_after_click(self, driver, wait):
        privacy_policy_button = wait.until(EC.element_to_be_clickable(self.locators.XPATH_PRIVACY_POLICY_BUTTON))
        self.driver.execute_script("arguments[0].click();", privacy_policy_button)
        self.driver.switch_to.window(driver.window_handles[1])
        assert self.driver.current_url == Links.PRIVACY_POLICY_URL


    def click_support_nav_menu(self):
        return self.driver.find_element(*self.locators.SUPPORT_MENU).click()


    def faq_submenu_should_be_visible(self, wait):
        element = wait.until(EC.visibility_of_element_located(self.locators.SUPPORT_FAQ_SUBMENU))
        assert element.is_displayed() and element.is_enabled(), f'"{element}" link is not visible or clickable'

