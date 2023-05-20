from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.main_page_locators import *
import requests
import os


class MainPage(BasePage):
    locators = MainPageLocators()

    def sample_function(self):
        return self


    def get_header_search_field_attribute(self, attribute):
        search_placeholder = self.driver.find_element(*MainPageLocators.HEADER_SEARCH_FIELD)
        return search_placeholder.get_attribute(attribute)
