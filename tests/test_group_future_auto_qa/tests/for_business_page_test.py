from tests.test_group_future_auto_qa.locators.for_business_page_locators import ForBusinessPageLocators
from tests.test_group_future_auto_qa.pages.for_business_page import ForBusinessPage


class TestBusinessPage:
    def test_tc_012_01_04_verify_the_headings_are_present_on_the_page(self, driver):
        business_page = ForBusinessPage(driver, ForBusinessPageLocators.FOR_BUSINESS_PAGE_URL)
        business_page.open_page()
        headers_count = business_page.check_headings()
        assert len(headers_count) == 7, "Not all headings are present on the page"

