from pages.base_page import BasePage
from locators.locators import PricingPageLocators as P, BasePageLocators as B
from test_data.all_links import Links


class PricingPage(BasePage):
    def verify_the_title_onecall_is_visible(self):
        title = self.driver.find_element(*P.LINK_TEXT_ONE_CALL)
        assert title.is_displayed()

    def visibility_two_buttons_detailed_pricing(self):
        for pricing_locator in P.button_detailed_pricing_locators:
            button = self.driver.find_element(*pricing_locator)
            assert button.is_displayed()


    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "Pricing"
        displayed_title = self.driver.find_element(*P.DISPLAYED_TITLE).text
        assert displayed_title == expected_title

    def verify_clicking_on_the_logo_from_page_Pricing_redirects_to_main_page(self):
        self.driver.find_element(*B.LOGO_LOCATOR).click()
        assert self.driver.current_url == Links.URL_MAIN_PAGE
