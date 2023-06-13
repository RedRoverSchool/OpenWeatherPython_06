from conftest import driver
from pages.pricing_page import PricingPage
from locators.locators import PricingPageLocators as P

class TestPricingPage:
    def test_TC_008_02_02_Visibility_the_title_OneCall_is_visible(self, driver):
        pricing_page = PricingPage(driver, link=P.URL_PRICING)
        pricing_page.open_page()
        pricing_page.verify_the_title_onecall_is_visible()

    def test_tc_008_03_01_visibility_two_buttons_pricing(self, driver):
        pricing_page = PricingPage(driver, link=P.URL_PRICING)
        pricing_page.open_page()
        pricing_page.visibility_two_buttons_detailed_pricing()
