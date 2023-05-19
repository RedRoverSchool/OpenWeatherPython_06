import time

from tests.test_JenyaPageObject.pages.base_page import BasePage
from tests.test_JenyaPageObject.locators.cookies_settings_page_locators import CookiesSettingsPageLocators

class CookiesSettingsPage(BasePage):
    locators = CookiesSettingsPageLocators()

    def check_cookies_settings_page_title(self):
        cookies_settings_title = self.element_is_visible(self.locators.TITLE_COOKIES_SETTINGS)
        time.sleep(5)
        return cookies_settings_title.is_displayed()
