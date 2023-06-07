from pages.weather_dashboard_page import WeatherDashboardPage


class TestWeatherDashboard:
    def test_tc_006_02_01_verify_display_of_how_to_start_section(self, driver, open_and_load_main_page):
        page = WeatherDashboardPage(driver)
        page.verify_display_of_how_to_start_section()

    def test_tc_006_02_03_weather_dashboard_verify_the_transition_to_another_page(self, driver,
                                                                                  open_and_load_main_page):
        page = WeatherDashboardPage(driver)
        page.transition_to_another_page()
