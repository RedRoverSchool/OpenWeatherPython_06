import pytest
from oldTests.test_group_100000.pages.pricing_page import *
from oldTests.test_group_100000.locators.pricing_page_locators import PricingLocators as P

def test_TC_008_02_02_Visibility_the_title_OneCall_is_visible(driver):
    pricing_page = PricingPage(driver, link=P.URL_PRICING)
    pricing_page.open_page()
    pricing_page.verify_the_title_onecall_is_visible()


