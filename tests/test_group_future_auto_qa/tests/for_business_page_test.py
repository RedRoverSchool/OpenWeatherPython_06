from tests.test_group_future_auto_qa.locators.for_business_page_locators import ForBusinessPageLocators
from tests.test_group_future_auto_qa.pages.for_business_page import ForBusinessPage


class TestBusinessPage:
    def test_tc_012_01_04_verify_the_headings_are_present_on_the_page(self, driver):
        business_page = ForBusinessPage(driver, ForBusinessPageLocators.FOR_BUSINESS_PAGE_URL)
        business_page.open_page()
        business_page.check_headings()

    def test_tc_012_01_06_verify_the_buttons_are_present_on_the_page(self, driver):
        business_page = ForBusinessPage(driver, ForBusinessPageLocators.FOR_BUSINESS_PAGE_URL)
        business_page.open_page()
        business_page.check_buttons()

    def test_tc_012_01_07_verify_the_elements_are_presented_on_the_page(self, driver):
        business_page = ForBusinessPage(driver, ForBusinessPageLocators.FOR_BUSINESS_PAGE_URL)
        business_page.open_page()
        business_page.check_elements()

