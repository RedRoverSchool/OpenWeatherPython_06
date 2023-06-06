from pages.dashboard_page import DashboardPage


class TestDashboardPage:
    def test_tc_001_05_03_Verify_humidity_percentage_in_detailed_weather_data_for_current_location(self, driver,
                                                                                                   open_and_load_main_page):
        page = DashboardPage(driver)
        page.verify_humidity_percentage_in_detailed_weather_data_for_current_location()

    def test_tc_006_02_01_verify_display_of_how_to_start_section(self, driver, open_and_load_main_page):
        page = DashboardPage(driver)
        page.verify_display_of_how_to_start_section()

    def test_tc_006_02_03_weather_dashboard_verify_the_transition_to_another_page(self, driver,
                                                                                  open_and_load_main_page):
        page = DashboardPage(driver)
        page.transition_to_another_page()
