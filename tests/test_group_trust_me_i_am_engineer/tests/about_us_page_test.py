from tests.test_group_trust_me_i_am_engineer.pages.about_us_page import AboutUsPage


def test_tc_001_15_01_verify_correct_header_about_us_page(driver, wait):
    page = AboutUsPage(driver)
    page.verify_correct_header_about_us_page(wait)


def test_tc_001_15_02_verify_image_beside_header_is_displayed(driver, wait):
    page = AboutUsPage(driver)
    page.verify_image_beside_header_is_displayed(wait)


def test_tc_001_15_05_there_are_five_headers_on_the_page_about_us_footer(driver, wait):
    page = AboutUsPage(driver)
    page.verify_there_are_five_headers_on_the_page_about_us_footer(wait)