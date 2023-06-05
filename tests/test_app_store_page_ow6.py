from pages.about_us_page import AboutUsPage
from pages.app_store_page import AppStorePage
from pages.main_page import MainPage


class TestAppStorePage:

    def test_tc_001_15_10_verify_redirection_to_app_store(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.go_to_about_us_page_from_main_page(driver)

        about_us_page = AboutUsPage(driver)
        about_us_page.click_on_app_store_button()

        app_store_page = AppStorePage(driver)
        app_store_page.verify_element_on_page_url()

