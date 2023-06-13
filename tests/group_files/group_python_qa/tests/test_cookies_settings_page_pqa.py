from tests.group_files.group_python_qa.pages.cookies_settings_page_pqa import CookiesSettings


class TestCookiesSettings:
    def test_tc_001_13_02_01_verify_the_savings_of_cookies_settings(self, driver, wait):
        settings_cookies_page = CookiesSettings(driver, URL_COOKIES_SETTINGS)
        settings_cookies_page.open_page()
        settings_cookies_page.turn_on_cookies_and_verify_cookies_savings(wait)

