from tests.test_group_roma.pages.main_page import MainPage


class TestMainPage:

    def test_TC_003_10_03_visibility_of_GitHub_icon(self, driver, open_and_load_main_page):
        main_page = MainPage(driver, open_and_load_main_page)
        main_page.go_to_footer(driver)
        main_page.is_GitHub_icon_displayed(driver)