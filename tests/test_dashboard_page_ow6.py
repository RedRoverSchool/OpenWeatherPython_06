from locators.locators import DashboardPageLocators
from pages.dashboard_page import Dashboard


class TestDashboardPage:

    def test_006_04_03_Verify_that_the_subscribe_button_are_clickable_in_the_Pricing_and_limits_section(self,
                                                                                                       driver):
        dashboard_page = Dashboard(driver, DashboardPageLocators.HEADER_DASHBOARD_LINK)
        dashboard_page.open_page()
        dashboard_page.subscribe_buttons_are_clickable()

    def test_TC_006_03_01_verify_display_of_client_logos(self, driver):
        page = Dashboard(driver, DashboardPageLocators.HEADER_DASHBOARD_LINK)
        page.open_page()
        page.verify_display_of_client_logos()

    def test_TC_006_04_01_Verify_display_of_Pricing_and_limits_section(self, driver):
        dashboard_page = Dashboard(driver, DashboardPageLocators.HEADER_DASHBOARD_LINK)
        dashboard_page.open_page()
        dashboard_page.verify_display_of_Pricing_and_limits_section()

