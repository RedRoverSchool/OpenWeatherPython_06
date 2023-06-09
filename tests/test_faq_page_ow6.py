from pages.faq_page import FAQPage
from test_data.all_links import Links

class TestFAQPage:

    def test_tc_015_01_04_hidden_text_is_displayed_by_clicking_on_accordion_buttons(self, driver):
        faq_page = FAQPage(driver, Links.FAQ_URL)
        faq_page.open_page()
        faq_page.check_hidden_text_is_displayed()

    def test_tc_002_03_09_open_faq(self, driver, open_and_load_main_page):
        faq_page = FAQPage(driver)
        faq_page.check_header_title("faq")
