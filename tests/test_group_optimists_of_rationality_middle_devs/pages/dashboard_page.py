from pages.base_page import BasePage
from tests.test_group_optimists_of_rationality_middle_devs.locators.dashboard_page_locators import DashboardLocators


class Dashboard(BasePage):
    locators = DashboardLocators

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
        logo = self.driver.find_element(*DashboardLocators.DASHBOARD_LOGO_IMAGE)
        assert logo.is_displayed(), 'Dynamic image with customer logos not showing up in the "Our users" section'