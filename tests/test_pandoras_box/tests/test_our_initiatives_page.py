from tests.test_pandoras_box.pages.our_initiatives_page import OurInitiativesPage


def test_010_02_02_check_title_student_initiatives(driver, open_and_load_main_page):
    our_initiatives = OurInitiativesPage(driver)
    our_initiatives.click_header_link('our initiatives')
    our_initiatives.verify_learn_more_link_redirects_to_valid_page()
