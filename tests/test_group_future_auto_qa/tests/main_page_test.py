from tests.test_group_future_auto_qa.pages.main_page import MainPage
import pytest


class TestMainPageHeader:
    def test_tc_002_02_07_placeholder_is_displayed_in_search_field(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        search_placeholder_text = main_page.get_header_search_field_attribute("placeholder")
        assert search_placeholder_text == "Weather in your city", \
            "Password field placeholder text is incorrect or missing"


    def test_tc_002_02_09_placeholder_disappears_if_symbol_is_typed_in_search_field(self, driver,
                                                                                           open_and_load_main_page,
                                                                                           wait):
        main_page = MainPage(driver)
        search_placeholder_text = main_page.get_header_search_field_attribute("placeholder")
        main_page.click_header_search_field()
        main_page.fill_city_search_field('a')
        assert search_placeholder_text not in main_page.get_header_search_field_attribute("value"), \
            "The placeholder text is still visible in the search field after typing a symbol"


    def test_tc_002_03_23_faq_link_is_visible_and_clickable(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.click_support_nav_menu()
        main_page.faq_submenu_should_be_visible(wait=wait)
