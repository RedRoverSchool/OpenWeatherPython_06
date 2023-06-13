from pages.base_page import BasePage
from oldTests.test_group_100000.locators.pricing_page_locators import PricingLocators as P


class PricingPage(BasePage):
    def verify_the_title_onecall_is_visible(self):
        title = self.driver.find_element(*P.LINK_TEXT_ONE_CALL)
        assert title.is_displayed()