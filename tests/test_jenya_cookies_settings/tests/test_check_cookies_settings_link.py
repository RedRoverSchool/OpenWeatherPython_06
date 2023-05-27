import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tests.test_JenyaPageObject.pages.cookies_settings_page import CookiesSettingsPage
from tests.test_JenyaPageObject.locators.cookies_settings_page_locators import CookiesSettingsPageLocators
#from conftest import wait


class TestCookiesSettingsLink():
    @pytest.fixture
    def open(self, driver, wait):
        url = "https://openweathermap.org/cookies-settings/"
        driver.get(url)
        yield driver
        driver.quit()

    @pytest.fixture()
    def wait(driver):
        wait = WebDriverWait(driver, 25)
        yield wait



    def test_TC_001_13_01_cookies_settings_title(self, driver, open):
        assert driver.find_element(*CookiesSettingsPageLocators.TITLE_COOKIES_SETTINGS).is_displayed()
    def test_TC_001_13_01_cookies_settings_analyse_radio_button_ON(self, driver, open):
        ON_button1 = driver.find_element(*CookiesSettingsPageLocators.COOKIES_ANALYSE_CHECKBOX_ON)
        assert ON_button1.is_displayed() and ON_button1.is_enabled(), "ON checkbox is not displayed or not enable"
    def test_TC_001_13_01_cookies_settings_analyse_radio_name_ON(self, driver, open):
        ON_button_name1 = driver.find_element(*CookiesSettingsPageLocators.COOKIES_ANALYSE_NAME_ON)
        assert ON_button_name1.is_displayed(), "ON button name is not visible"
    def test_TC_001_13_01_cookies_settings_analyse_radio_button_OFF(self, driver, open):
        OFF_button1 = driver.find_element(*CookiesSettingsPageLocators.COOKIES_ANALYSE_CHECKBOX_OFF)
        assert OFF_button1.is_displayed() and OFF_button1.is_selected(), "OFF checkbox is not displayed or not selected"
    def test_TC_001_13_01_cookies_settings_analyse_radio_name_OFF(self, driver, open):
        OFF_button1 = driver.find_element(*CookiesSettingsPageLocators.COOKIES_ANALYSE_NAME_OFF)
        assert OFF_button1.is_displayed(), "OFF button name is not visible"



    def test_TC_001_13_01_cookies_settings_advertising_radio_button_ON(self, driver, open):
        ON_button2 = driver.find_element(*CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_CHECKBOX_ON)
        assert ON_button2.is_displayed() and ON_button2.is_enabled(), "ON checkbox is not displayed or not enable"
    def test_TC_001_13_01_cookies_settings_advertising_radio_name_ON(self, driver, open):
        ON_button2 = driver.find_element(*CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_NAME_ON)
        assert ON_button2.is_displayed(), "ON button is not visible"
    def test_TC_001_13_01_cookies_settings_advertising_radio_button_OFF(self, driver, open):
        OFF_button2 = driver.find_element(*CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_CHECKBOX_OFF)
        assert OFF_button2.is_displayed() and OFF_button2.is_selected(), "OFF checkbox is not displayed or not selected"
    def test_TC_001_13_01_cookies_settings_advertising_radio_name_OFF(self, driver, open):
        OFF_button2 = driver.find_element(*CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_NAME_OFF)
        assert OFF_button2.is_displayed(), "OFF button name is not visible"



    def test_TC_001_13_01_cookies_settings_Save_changes_button_presence(self, driver, open):
        button = driver.find_element(*CookiesSettingsPageLocators.SAVE_CHANGES_BUTTON)
        assert button.is_displayed()

    def test_TC_001_13_01_cookies_settings_save_changes(self, driver, open):
        footer = driver.find_element(*CookiesSettingsPageLocators.FOOTER)
        footer.click()

        action = ActionChains(driver)
        action.move_to_element(
            driver.find_element(*CookiesSettingsPageLocators.COOKIES_ANALYSE_CHECKBOX_ON)).click().perform()
        action.move_to_element(
            driver.find_element(*CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_CHECKBOX_ON)).click().perform()
        action.move_to_element(
            driver.find_element(*CookiesSettingsPageLocators.SAVE_CHANGES_BUTTON)).click().perform()
        assert driver.find_element(*CookiesSettingsPageLocators.COOKIES_SAVED_MESSAGE).is_displayed()




    @pytest.mark.parametrize("locator, expected_visibility, expected_enabled", [
        (CookiesSettingsPageLocators.COOKIES_ANALYSE_CHECKBOX_ON, True, True),
        (CookiesSettingsPageLocators.COOKIES_ANALYSE_NAME_ON, True, True),
        (CookiesSettingsPageLocators.COOKIES_ANALYSE_CHECKBOX_OFF, True, True),
        (CookiesSettingsPageLocators.COOKIES_ANALYSE_NAME_OFF, True, True),
        (CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_CHECKBOX_ON, True, True),
        (CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_NAME_ON, True, True),
        (CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_CHECKBOX_OFF, True, True),
        (CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_NAME_OFF, True, True),
    ])
    def test_TC_001_13_01_cookies_settings_visibility_and_enabled(self, driver, open, locator, expected_visibility, expected_enabled):
        element = driver.find_element(*locator)
        assert element.is_displayed() == expected_visibility and element.is_enabled() == expected_enabled


















