from tests.test_group_optimists_of_rationality_middle_devs.locators.main_page_locators import MainPageLocators
from locators.locators import DashboardPageLocators
from pages.base_page import BasePage


class Dashboard(BasePage):
    locators = DashboardPageLocators

    def subscribe_buttons_are_clickable(self):
        clickable_elements = self.check_links_are_clickable()
        assert all(clickable_elements), "Not all Subscribe links are clickable"

    def check_elements(self):
        subscribe_links = self.element_is_present(self.locators.PRICING_PLANS_SUBSCRIBE)
        subscribe_links1 = self.element_is_present(self.locators.PRICING_PLANS_SUBSCRIBE1)
        subscribe_links2 = self.element_is_present(self.locators.PRICING_PLANS_SUBSCRIBE2)
        subscribe_links3 = self.element_is_present(self.locators.PRICING_PLANS_SUBSCRIBE3)
        return [subscribe_links, subscribe_links1, subscribe_links2, subscribe_links3]

    def check_links_are_clickable(self):
        links = self.check_elements()
        return [element.is_enabled() for element in links]

    def verify_display_of_client_logos(self):
        logo = self.driver.find_element(*MainPageLocators.DASHBOARD_LOGO_IMAGE)
        assert logo.is_displayed(), 'Dynamic image with customer logos not showing up in the "Our users" section'

    def verify_display_of_Pricing_and_limits_section(self):
        pricing_and_limits_section_elements = self.check_sections_are_display()
        assert all(pricing_and_limits_section_elements), 'No "pricing and limits" module'

    def check_pricing_and_limits_section(self):
        pricing_and_limits_section = self.element_is_present(self.locators.PRICING_AND_LIMITS)
        pricing_and_limits_section1 = self.element_is_present(self.locators.PRICING_AND_LIMITS1)
        pricing_and_limits_section2 = self.element_is_present(self.locators.PRICING_AND_LIMITS2)
        return [pricing_and_limits_section, pricing_and_limits_section1, pricing_and_limits_section2]

    def check_sections_are_display(self):
        links = self.check_pricing_and_limits_section()
        return [element.is_displayed() for element in links]

    def verify_sign_up_button_is_clickable(self):
        sign_up_button = self.driver.find_element(*MainPageLocators.PRICING_PLANS_SIGN_UP)
        assert sign_up_button.is_enabled(), "Sign up link is not clickable"

