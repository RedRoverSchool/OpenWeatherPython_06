from pages.base_page import BasePage
from locators.locators import CookiesSettingsPageLocators

class CookiesSettingsPage(BasePage):
    def scroll_page_down_to_chekboxes_and_button(self):
        save_changes_button = self.driver.find_element(*CookiesSettingsPageLocators.SAVE_CHANGES_BUTTON)
        self.driver.execute_script("arguments[0].focus();", save_changes_button)

    def click_cookies_that_analyse_radiobutton(self, wait):
        cookies_that_analyse_radiobutton = self.driver.\
            find_element(*CookiesSettingsPageLocators.RADIO_BUTTON_1)
        cookies_that_analyse_radiobutton.click()

    def click_google_advertising_radiobutton(self, wait):
        google_advertising_radiobutton = self.driver.\
            find_element(*CookiesSettingsPageLocators.RADIO_BUTTON_3)
        google_advertising_radiobutton.click()

    def click_save_changes_button(self, wait):
        save_changes_button = self.driver.find_element(*CookiesSettingsPageLocators.SAVE_CHANGES_BUTTON)
        save_changes_button.click()

    def verify_successful_message_appears(self, wait):
        expected_message = 'Your cookie settings were saved'
        successful_message = self.driver.find_element(*CookiesSettingsPageLocators.SUCCESSFUL_SAVING_SETTINGS_MESSAGE)
        assert expected_message in successful_message.text, "Message not found"


