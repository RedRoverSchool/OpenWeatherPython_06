from pages.main_page import MainPage
from locators.locators import MainPageLocators


class TestMainPage:

    def test_example_search_city(self, driver, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.search_city('Almaty')

    def test_tc_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.search_city("Paris")
        main_page.choose_1st_option(wait)
        main_page.switch_to_c_temp()
        main_page.check_8_lines_are_displayed()

    def test_tc_021_01_01_visibility_of_agriculture_analytics_link(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.element_is_displayed(MainPageLocators.AGRICULTURE_ANALYTICS_TITLE_LOCATOR, wait)


