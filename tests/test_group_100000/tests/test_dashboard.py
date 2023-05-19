from tests.test_group_100000.pages.dashboard_page import DashboardPage


def test_TC_006_02_01_verify_display_of_how_to_start_section(driver, open_and_load_main_page):
    page = DashboardPage(driver)
    page.verify_display_of_how_to_start_section()