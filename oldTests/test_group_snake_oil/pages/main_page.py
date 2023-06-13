from pages.base_page import BasePage
from oldTests.test_group_snake_oil.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators

    def check_visibility_of_linkedIn_icon(self):
        element = self.element_is_visible(self.locators.LINKEDIN_ICON)
        assert element.is_displayed(), "LinkedIn interactive icon is not visible on a page"

    def check_clickability_of_linkedIn_icon(self):
        element = self.element_is_clickable(self.locators.LINKEDIN_ICON)
        assert element.is_enabled(), "LinkedIn interactive icon is not clickable on a page"

    def open_Support_dropdown(self):
        wait(self.driver, timeout=10).until(EC.invisibility_of_element_located(self.locators.OVERLAY_LOCATOR))
        dropdown = wait(self.driver, timeout=10).until(EC.element_to_be_clickable(self.locators.SUPPORT_DROPDOWN))
        dropdown.click()

    def check_visibility_of_FAQ_element(self):
        element = self.element_is_visible(self.locators.FAQ_ELEMENT)
        assert element.is_displayed(), "FAQ element is not visible on the page"

    def check_click_FAQ_element(self):
        element = self.element_is_clickable(self.locators.FAQ_ELEMENT)
        assert element.is_enabled(), "FAQ element is not clickable on the page"
