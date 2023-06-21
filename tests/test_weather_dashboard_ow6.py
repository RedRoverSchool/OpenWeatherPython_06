from pages.weather_dashboard_page import WeatherDashboardPage
from test_data.urls import WeatherDashboardUrls


class TestWeatherDashboard:
    def test_tc_006_02_01_verify_display_of_how_to_start_section(self, driver, open_and_load_main_page):
        page = WeatherDashboardPage(driver)
        page.verify_display_of_how_to_start_section()

    def test_tc_006_02_03_weather_dashboard_verify_the_transition_to_another_page(self, driver,
                                                                                  open_and_load_main_page):
        page = WeatherDashboardPage(driver)
        page.transition_to_another_page()

    def test_TC_006_04_04_pricing_plans_are_visible(self, driver):
        page = WeatherDashboardPage(driver, link=WeatherDashboardUrls.dashboard_URL)
        page.open_page()
        page.check_pricing_plans()
