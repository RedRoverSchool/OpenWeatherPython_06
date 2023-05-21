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

