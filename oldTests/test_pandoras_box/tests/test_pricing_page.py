from oldTests.test_pandoras_box.pages.pricing_page import PricingPage


def test_tc_002_03_08_open_pricing(driver, open_and_load_main_page):
    pricing_page = PricingPage(driver)
    pricing_page.check_header_title("pricing")


def test_tc_008_03_01_visibility_two_buttons_pricing(driver):
    pricing_page = PricingPage(driver,link = PricingPage.pricing_url)
    pricing_page.open_page()
    pricing_page.visibility_two_buttons_detailed_pricing()
