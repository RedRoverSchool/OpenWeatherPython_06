from pages.base_page import BasePage
from tests.tests_group_optimists_of_rationality_middle_devs.locators.main_page_locators import *

class MainPage(BasePage):
    locators = MainPageLocators()

    def sample_function(self):
        return self
