from tests.group_files.group_zmeyki.pages.dashboard_page import DashboardPage


class TestDashboardPage:

    def test_tc_006_01_09_verify_hourly_forecast_api_link_redirects_to_valid_page(self, driver, wait):
        dashboard_page = DashboardPage(driver, link='https://openweathermap.org/weather-dashboard')
        dashboard_page.open_page()
        dashboard_page.verify_hourly_forecast_api_link_redirects_to_valid_page(wait=wait)
