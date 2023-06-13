from pages.base_page import BasePage
from tests.group_files.group_python_qa.locators.locators import CookiesSettingsLocators


class CookiesSettings(BasePage):
    locator = CookiesSettingsLocators()

    def turn_on_cookies_and_verify_cookies_savings(self, wait):
        self.allow_all_cookies()
        self.find_element_and_click(CookiesSettingsLocators.RADIOBUTTON_1_LOCATOR)
        self.find_element_and_click(CookiesSettingsLocators.RADIOBUTTON_2_LOCATOR)
        self.find_element_and_click(CookiesSettingsLocators.SAVE_CHANGES_BUTTON)
        self.element_is_displayed(CookiesSettingsLocators.ALERT_BANNER, wait)
