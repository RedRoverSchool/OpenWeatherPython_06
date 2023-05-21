from pages.base_page import BasePage
from tests.test_group_snake_oil.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    locators = MainPageLocators

    def allow_all_cookies(self):
        self.element_is_clickable(self.locators.ALLOW_ALL_COOKIES).click()

    def check_visibility_of_linkedIn_icon(self):
        return self.element_is_visible(self.locators.LINKEDIN_ICON)

    def check_clickability_of_linkedIn_icon(self):
        return self.element_is_clickable(self.locators.LINKEDIN_ICON)