from tests.test_pandoras_box.pages.api_page import APIPage


def test_005_17_01_check_title_history_api_full_archive(driver, open_and_load_main_page):
    history_api_full = APIPage(driver)
    history_api_full.click_header_link('api')
    history_api_full.click_button_api_doc_history_full_archive()
    history_api_full.check_title_history_api_full_archive()

