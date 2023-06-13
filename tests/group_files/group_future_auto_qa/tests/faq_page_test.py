from tests.group_files.group_future_auto_qa.pages.faq_page import FAQPage

def test_tc_015_01_04_hidden_text_is_displayed_by_clicking_on_accordion_buttons(driver, open_and_load_main_page, wait):
    faq_page = FAQPage(driver)
    faq_page.open_faq_page()
    faq_page.check_hidden_text_is_displayed()
