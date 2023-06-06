from pages.about_us_page import AboutUsPage
from pages.main_page import MainPage


class TestAboutUsPage:

    def test_tc_001_15_01_verify_correct_header_about_us_page(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.go_to_about_us_page_from_main_page(driver)

        about_us_page = AboutUsPage(driver)
        about_us_page.verify_correct_header_about_us_page()

    def test_tc_001_15_02_verify_image_beside_header_is_displayed(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.go_to_about_us_page_from_main_page(driver)

        about_us_page = AboutUsPage(driver)
        about_us_page.verify_image_beside_header_is_displayed()

    def test_tc_001_15_05_there_are_five_headers_on_the_page_about_us_footer(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.go_to_about_us_page_from_main_page(driver)

        about_us_page = AboutUsPage(driver)
        about_us_page.verify_five_headers_on_the_page_about_us_footer()

    def test_tc_001_15_11_verify_cursor_transformation_after_hovering_over_on_element(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.go_to_about_us_page_from_main_page(driver)

        about_us_page = AboutUsPage(driver)
        element = about_us_page.element_is_visible(about_us_page.locators.BYU_BY_SUBSCRIPTIONS)
        about_us_page.check_cursor_style_transformation(element)


