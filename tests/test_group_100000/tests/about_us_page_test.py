from tests.test_group_100000.pages.about_us_page import AboutUsPage


def test_tc_001_15_12_verify_correct_header_about_us_page(driver, wait):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()

    about_us_page.verify_correct_header_about_us_page()