from pages.base_page import BasePage
from tests.test_the_hardworking_club.locators.locators_all import WidgetsPageLocators
from conftest import driver


class WidgetsPage(BasePage):
    locators = WidgetsPageLocators()

    def check_input_fields(self):
        fields = self.driver.find_elements(*self.locators.INPUT_FIELDS)
        for field in fields:
            assert field.is_displayed()







