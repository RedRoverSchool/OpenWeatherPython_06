from tests.test_pandoras_box.pages.faq_page import FaqPage


def test_tc_002_03_09_open_faq(driver, open_and_load_main_page):
    faq_page = FaqPage(driver)
    faq_page.check_header_title("faq")