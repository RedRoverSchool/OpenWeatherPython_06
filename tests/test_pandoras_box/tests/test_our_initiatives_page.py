from tests.test_pandoras_box.pages.our_initiatives_page import OurInitiativesPage


def test_tc_010_02_02_open_our_initiatives(driver, open_and_load_main_page):
    our_initiatives_page = OurInitiativesPage(driver)
    our_initiatives_page.check_header_title("our initiatives")
