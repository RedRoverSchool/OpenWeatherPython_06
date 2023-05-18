from tests.test_pandoras_box.pages.pricing_page import PricingPage


def test_tc_002_03_08_open_pricing(driver, open_and_load_main_page):
    pricing_page = PricingPage(driver)
    pricing_page.check_header_title("pricing")