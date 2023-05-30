from tests.test_group_python_qa.pages.our_initiatives_page import OurInitiativesPage


def test_002_01_11_verify_main_logo(driver):
    our_initiatives_page = OurInitiativesPage(driver)
    our_initiatives_page.verify_main_logo()

