from tests.test_group_lutz_squad.pages.cookies_settings_page import CookiesSettingsPage
from tests.test_group_lutz_squad.locators.cookies_settings_page_locators import \
    CookiesSettingsPageLocators as CS


def test_TC_001_13_02_verify_the_saving_of_cookies_settings(driver, wait):
    page = CookiesSettingsPage(driver, link=CS.COOKIES_SETTINGS_PAGE_LINK)
    page.open_page()
    page.scroll_page_down_to_checkboxes_and_button()
    page.click_cookies_that_analyse_radiobutton(wait)
    page.click_google_advertising_radiobutton(wait)
    page.click_save_changes_button(wait)
    page.verify_successful_message_appears(wait)
