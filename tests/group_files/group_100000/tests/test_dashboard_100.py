from tests.group_files.group_100000.pages.dashboard_page import DashboardPage


def test_TC_001_05_03_Verify_humidity_percentage_in_detailed_weather_data_for_current_location(driver,
                                                                                               open_and_load_main_page):
    page = DashboardPage(driver)
    page.verify_humidity_percentage_in_detailed_weather_data_for_current_location()


def test_TC_006_02_01_verify_display_of_how_to_start_section(driver, open_and_load_main_page):
    page = DashboardPage(driver)
    page.verify_display_of_how_to_start_section()


def test_TC_006_02_03_weather_dashboard_verify_the_transition_to_another_page(driver, open_and_load_main_page):
    page = DashboardPage(driver)
    page.transition_to_another_page()
