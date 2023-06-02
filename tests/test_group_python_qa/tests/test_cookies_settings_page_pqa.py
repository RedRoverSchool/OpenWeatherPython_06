from conftest import driver
from tests.test_group_python_qa.pages.cookies_settings_page_pqa import CookiesSettings
from tests.test_group_python_qa.links.links_all_pages import *
from tests.test_group_python_qa.locators.locators import CookiesSettingsLocators


def test_tc_001_13_02_01_verify_the_savings_of_cookies_settings(driver):
    settings_cookies_page = CookiesSettings(driver, URL_COOKIES_SETTINGS)
    settings_cookies_page.open_page()
    settings_cookies_page.find_element_and_click(CookiesSettingsLocators.ALLOW_BUTTON)
    settings_cookies_page.find_element_and_click(CookiesSettingsLocators.RADIOBUTTON_1_LOCATOR)
    settings_cookies_page.find_element_and_click(CookiesSettingsLocators.RADIOBUTTON_2_LOCATOR)
    settings_cookies_page.find_element_and_click(CookiesSettingsLocators.SAVE_CHANGES_BUTTON)

