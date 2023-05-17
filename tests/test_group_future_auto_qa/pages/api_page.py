from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.api_page_locators import *
import requests
import os


class ApiPage(BasePage):
    locators = ApiPageLocators()

    def sample_function(self):
        return self



