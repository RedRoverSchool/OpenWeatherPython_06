from pages.cookies_settings_page import CookiesSettingsPage
from test_data.urls import CookiesSettingPageUrls

class TestCookiesSettingsPage:
    def test_TC_001_13_02_verify_the_saving_of_cookies_settings(self, driver, wait):
        page = CookiesSettingsPage(driver, CookiesSettingPageUrls.COOKIES_SETTINGS)
        page.open_page()
        page.scroll_page_down_to_chekboxes_and_button()
        page.click_cookies_that_analyse_radiobutton(wait)
        page.click_google_advertising_radiobutton(wait)
        page.click_save_changes_button(wait)
        page.verify_successful_message_appears(wait)
