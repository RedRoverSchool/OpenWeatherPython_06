from tests.test_pandoras_box.pages.our_initiatives_page import OurInitiativesPage


def test_010_02_02_check_title_student_initiatives(driver, open_and_load_main_page):
    our_initiatives = OurInitiativesPage(driver)
    our_initiatives.click_header_link('our initiatives')
    our_initiatives.verify_learn_more_link_redirects_to_valid_page()


def test_tc_010_01_04_check_url_our_initiatives(driver, open_and_load_main_page):
    our_initiatives = OurInitiativesPage(driver)
    our_initiatives.click_header_link('our initiatives')
    our_initiatives.verify_correct_url_out_initiative()

    

def test_010_01_01_1_text_on_button_learn_more(driver, open_and_load_main_page):
    our_initiatives = OurInitiativesPage(driver)
    our_initiatives.click_header_link('our initiatives')
    our_initiatives.check_text_on_button_learn_more()
