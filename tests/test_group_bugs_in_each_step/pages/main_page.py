from pages.base_page import BasePage
from tests.test_group_bugs_in_each_step.locators.main_page_locators import *
import requests
import os

class MainPage(BasePage):
    locators = MainPageLocators()

    def sample_function(self):
        return self

