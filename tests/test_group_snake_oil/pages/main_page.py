from pages.base_page import BasePage
from tests.test_group_snake_oil.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    locators = MainPageLocators

    def check_visibility_of_linkedIn_icon(self):
        element = self.element_is_visible(self.locators.LINKEDIN_ICON)
        assert element.is_displayed(), "LinkedIn interactive icon is not visible on a page"

    def check_clickability_of_linkedIn_icon(self):
        element = self.element_is_clickable(self.locators.LINKEDIN_ICON)
        assert element.is_enabled(), "LinkedIn interactive icon is not clickable on a page"
