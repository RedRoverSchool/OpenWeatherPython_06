from pages.base_page import BasePage
from tests.test_group_snake_oil.locators.footer_locators import FootersLocators


class Footer(BasePage):
    locators = FootersLocators

    def find_technologies_module(self):
        return self.driver.find_element(*self.locators.FOOTER_TECHNOLOGIES)
