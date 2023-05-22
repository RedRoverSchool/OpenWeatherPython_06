from pages.base_page import BasePage
from tests.test_group_bugs_in_each_step.locators.main_page_locators import *
import requests
import os


class MainPage(BasePage):
    locators = MainPageLocators()

    def sample_function(self):
        return self

    def check_historical_weather_data_link_is_visible(self):
        historical_weather_data_link = self.element_is_visible(self.locators.HISTORICAL_WEATHER_DATA)
        return historical_weather_data_link.is_displayed()

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