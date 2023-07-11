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

    def test_tc_002_03_08_open_pricing(self, driver, open_and_load_main_page):
        pricing_page = PricingPage(driver)
        pricing_page.check_header_title("pricing")

    def test_TC_002_01_07_verify_clicking_on_the_logo_from_page_Pricing_redirects_to_main_page(self, driver):
        price_page = PricingPage(driver, P.URL_PRICING)
        price_page.open_page()
        price_page.verify_clicking_on_the_logo_from_page_Pricing_redirects_to_main_page()

    def test_TC_008_01_01_one_call_subscribe_button_redirects(self, driver):
        pricing_page = PricingPage(driver)
        pricing_page.check_one_call_subscribe_button_redirect()

