from conftest import driver
from pages.pricing_page import PricingPage
from locators.locators import PricingPageLocators as P

class TestPricingPage:
    def test_TC_008_02_02_Visibility_the_title_OneCall_is_visible(self, driver):
        pricing_page = PricingPage(driver, link=P.URL_PRICING)
        pricing_page.open_page()
        pricing_page.verify_the_title_onecall_is_visible()

    def test_tc_002_03_08_open_pricing(self, driver, open_and_load_main_page):
        pricing_page = PricingPage(driver)
        pricing_page.check_header_title("pricing")
