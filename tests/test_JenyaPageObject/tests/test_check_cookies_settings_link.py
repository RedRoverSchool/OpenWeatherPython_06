import pytest
from selenium.webdriver.common.by import By

from tests.test_JenyaPageObject.pages.cookies_settings_page import CookiesSettingsPage
from tests.test_JenyaPageObject.locators.cookies_settings_page_locators import CookiesSettingsPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class TestCookiesSettingsLink():
    @pytest.fixture
    def open(self, driver, wait):
        url = "https://openweathermap.org/cookies-settings/"
        driver.get(url)
        yield driver
        driver.quit()

    def test_TC_001_13_01_cookies_settings_title(self, driver):
        cookies_settings_page = CookiesSettingsPage(driver, "https://openweathermap.org/cookies-settings/")
        cookies_settings_page.open()
        title = cookies_settings_page.check_cookies_settings_page_title()
        assert title == True
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

    def test_cookies_settings_scroll_and_save(self, driver, open):

        first_button = driver.find_element(*CookiesSettingsPageLocators.COOKIES_ANALYSE_CHECKBOX_ON)
        driver.execute_script("arguments[0].scrollIntoView();", first_button)
        assert first_button.is_displayed() and first_button.is_enabled()
        driver.execute_script("arguments[0].click();", first_button)

        second_button = driver.find_element(*CookiesSettingsPageLocators.COOKIES_GOOGLE_ADVERTISING_CHECKBOX_ON)
        driver.execute_script("arguments[0].scrollIntoView();", second_button)
        assert second_button.is_displayed() and second_button.is_enabled()# Выбрать вторую радиокнопку
        driver.execute_script("arguments[0].click();", second_button)

        save_button = driver.find_element(*CookiesSettingsPageLocators.SAVE_CHANGES_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", save_button)

        assert save_button.is_displayed() and save_button.is_enabled()

        driver.execute_script("arguments[0].click();", save_button)

        message = driver.find_element(*CookiesSettingsPageLocators.COOKIES_SAVED_MESSAGE)
        assert message.text == "Your cookie settings were saved"
















