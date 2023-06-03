from pages.main_page import MainPage


class TestMainPage:
    def test_example_search_city(self, driver, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.search_city('Almaty')

