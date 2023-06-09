from locators.locators import DashboardPageLocators
from pages.dashboard_page import DashboardPage


class TestDashboardPage:

    def test_006_04_03_Verify_that_the_subscribe_button_are_clickable_in_the_Pricing_and_limits_section(self,
                                                                                                        driver):
        dashboard_page = DashboardPage(driver, DashboardPageLocators.HEADER_DASHBOARD_LINK)
        dashboard_page.open_page()
        dashboard_page.subscribe_buttons_are_clickable()

    def test_TC_006_03_01_verify_display_of_client_logos(self, driver):
        page = DashboardPage(driver, DashboardPageLocators.HEADER_DASHBOARD_LINK)
        page.open_page()
        page.verify_display_of_client_logos()

    def test_TC_006_04_01_Verify_display_of_Pricing_and_limits_section(self, driver):
        dashboard_page = DashboardPage(driver, DashboardPageLocators.HEADER_DASHBOARD_LINK)
        dashboard_page.open_page()
        dashboard_page.verify_display_of_Pricing_and_limits_section()

    def test_TC_006_04_02_Verify_that_the_Sign_up_button_is_clickable_in_the_Pricing_and_limits_section(self, driver):
        dashboard_page = DashboardPage(driver, DashboardPageLocators.HEADER_DASHBOARD_LINK)
        dashboard_page.open_page()
        dashboard_page.verify_sign_up_button_is_clickable()

    def test_tc_006_01_05_image_is_visible(self, driver, open_and_load_main_page):
        dash_page = DashboardPage(driver, DashboardPageLocators.HEADER_DASHBOARD_LINK)
        dash_page.open_page()
        dash_page.click_dashboard_link()
        dash_page.check_image_is_visible()

    def test_tc_006_01_09_verify_hourly_forecast_api_link_redirects_to_valid_page(self, driver, wait):
        dashboard_page = DashboardPage(driver, link='https://openweathermap.org/weather-dashboard')
        dashboard_page.open_page()
        dashboard_page.verify_hourly_forecast_api_link_redirects_to_valid_page(wait=wait)
