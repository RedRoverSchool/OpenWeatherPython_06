from tests.test_group_snake_oil.links.all_links import HOME_PAGE_URL
from tests.test_group_snake_oil.pages.main_page import MainPage


class TestMainPage:

    def test_tc_003_10_06_verify_linkedIn_link_is_visible(self, driver):
        main_page = MainPage(driver, HOME_PAGE_URL)
        main_page.open_page()
        main_page.check_visibility_of_linkedIn_icon()

    def test_tc_003_10_08_verify_linkedIn_link_is_clickable(self, driver):
        main_page = MainPage(driver, HOME_PAGE_URL)
        main_page.open_page()
        main_page.check_clickability_of_linkedIn_icon()

    def test_tc_015_01_01_verify_support_faq_is_visible(self, driver):
        support_page = MainPage(driver, HOME_PAGE_URL)
        support_page.open_page()
        support_page.open_Support_dropdown()
        support_page.check_visibility_of_FAQ_element()

    def test_tc_015_01_02_verify_support_faq_is_clickable(self, driver):
        support_page = MainPage(driver, HOME_PAGE_URL)
        support_page.open_page()
        support_page.open_Support_dropdown()
        support_page.check_click_FAQ_element()
