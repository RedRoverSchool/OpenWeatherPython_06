import time
from selenium.webdriver.support import expected_conditions as EC

import pytest

from conftest import wait
from tests.test_JenyaPageObject.pages.base_page import BasePage
from tests.test_JenyaPageObject.locators.cookies_settings_page_locators import CookiesSettingsPageLocators

class CookiesSettingsPage(BasePage):
    locators = CookiesSettingsPageLocators()
    url = "https://openweathermap.org/cookies-settings/"

    def open_cookies_settings_page(self):
        self.open()

    def check_cookies_settings_page_title(self):
        cookies_settings_title = self.element_is_visible(self.locators.TITLE_COOKIES_SETTINGS)
        time.sleep(5)
        return cookies_settings_title.is_displayed()



