from conftest import URL
from tests.test_group_future_auto_qa.pages.for_business_page import ForBusinessPage


class TestBusinessPage:
    def test_tc_012_01_04_verify_the_headings_are_present_on_the_page(self, driver):
        business_page = ForBusinessPage(driver, URL)
        business_page.open_page()
        assert business_page.check_headings(), "No headings are present on the page"

