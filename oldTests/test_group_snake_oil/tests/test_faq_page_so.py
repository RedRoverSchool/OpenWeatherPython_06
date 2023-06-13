from oldTests.test_group_snake_oil.links.all_links import HOME_PAGE_URL
from oldTests.test_group_snake_oil.pages.faq_page import FAQPage
from oldTests.test_group_snake_oil.pages.main_page import MainPage
from oldTests.test_group_snake_oil.links.all_links import FAQ_URL


class TestFaqPage:

    def test_tc_015_01_03_verify_support_faq_page_redirection(self, driver):
        main_page = MainPage(driver, HOME_PAGE_URL)
        main_page.open_page()
        main_page.open_Support_dropdown()
        faq_page = FAQPage(driver, FAQ_URL)
        faq_page.check_redirection_of_FAQ_element()
