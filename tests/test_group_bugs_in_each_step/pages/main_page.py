from pages.base_page import BasePage
from tests.test_group_bugs_in_each_step.locators.main_page_locators import *
import requests
import os


class MainPage(BasePage):
    locators = MainPageLocators()

    def sample_function(self):
        return self

    def check_historical_weather_data_link_is_visible(self):
        historical_weather_data_link = self.element_is_visible(self.locators.HISTORICAL_WEATHER_DATA_LINK)
        return historical_weather_data_link.is_displayed()

    def check_historical_weather_data_link_functionality(self):
        historical_weather_data_link = self.driver.find_element(*self.locators.HISTORICAL_WEATHER_DATA_LINK)
        self.go_to_element(historical_weather_data_link)
        historical_weather_data_link.click()
        assert '/api#history' in self.driver.current_url, \
            "The Historical Weather Data link leads to an incorrect page"

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

    def verify_how_to_start_visibility(self):
        how_to_start = self.driver.find_element(*self.locators.HOW_TO_START)
        assert how_to_start.is_displayed(), "The How to start link is not visible"


