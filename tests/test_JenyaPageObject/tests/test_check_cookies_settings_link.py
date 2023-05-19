from tests.test_JenyaPageObject.pages.cookies_settings_page import CookiesSettingsPage
from tests.test_JenyaPageObject.locators.cookies_settings_page_locators import CookiesSettingsPageLocators


class TestCookiesSettingsLink:

    def test_TC_001_13_01_cookies_settings_title(self, driver):
        cookies_settings_page = CookiesSettingsPage(driver, "https://openweathermap.org/cookies-settings/")
        cookies_settings_page.open()
        title = cookies_settings_page.check_cookies_settings_page_title()
        assert title == True

    def test_TC_001_13_01_cookies_settings_analyse_radio_button_ON(self, driver):
        analyse_ON = driver.find_element(*COOKIES_ANALYSE_CHECKBOX_ON)
        analyse_ON
