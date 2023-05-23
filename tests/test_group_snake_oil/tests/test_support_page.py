from tests.test_group_snake_oil.links.all_links import HOME_PAGE_URL
from tests.test_group_snake_oil.pages.support_page import SupportPage


class TestSupportPage:

    def test_tc_015_01_01_verify_support_faq_is_visible(self, driver):
        support_page = SupportPage(driver, HOME_PAGE_URL)
        support_page.open_page()
        support_page.check_visibility_and_clickablity_of_Support_dropdown()
        support_page.check_visibility_of_FAQ_element()
