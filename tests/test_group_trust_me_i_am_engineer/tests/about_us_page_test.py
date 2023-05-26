from tests.test_group_trust_me_i_am_engineer.pages.about_us_page import AboutUsPage


def test_tc_001_15_01_verify_correct_header_about_us_page(driver, wait):
    page = AboutUsPage(driver)
    page.verify_correct_header_about_us_page(wait)