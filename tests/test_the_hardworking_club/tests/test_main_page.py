from tests.test_the_hardworking_club.pages.main_page import MainPage


class TestMainPage:

    def test_TC_003_12_06_verify_privacy_policy_is_opened_after_click(self, driver, wait):
        main_page = MainPage(driver)
        main_page.verify_privacy_policy_is_opened_after_click(driver, wait)
