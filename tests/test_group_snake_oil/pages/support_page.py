from pages.base_page import BasePage
from tests.test_group_snake_oil.locators.support_locators import SupportPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class SupportPage(BasePage):
    locators = SupportPageLocators

    def check_visibility_and_clickablity_of_Support_dropdown(self):
        overlay_locator = (By.CLASS_NAME, "owm-loader")

        wait(self.driver, timeout=10).until(EC.invisibility_of_element_located(overlay_locator))
        dropdown = wait(self.driver, timeout=10).until(EC.element_to_be_clickable(self.locators.Support_dropdown))
        dropdown.click()
        assert dropdown.is_enabled(), "Dropdown element is not clicked"

    def check_visibility_of_FAQ_element(self):
        element = self.element_is_visible(self.locators.FAQ_element)
        assert element.is_displayed(), "FAQ element is not clickable on the page"

