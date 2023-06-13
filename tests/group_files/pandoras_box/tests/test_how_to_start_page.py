from tests.group_files.pandoras_box.pages.how_to_start_page import HowToStartPage


def test_tc_002_03_09_open_faq(driver, open_and_load_main_page):
    how_to_start_page = HowToStartPage(driver)
    how_to_start_page.check_header_title("how to start")