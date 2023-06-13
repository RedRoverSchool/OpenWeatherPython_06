from oldTests.test_pandoras_box.pages.dashboard_page import Dashboard


def test_tc_006_01_05_image_is_visible(driver, open_and_load_main_page):
    dash_page = Dashboard(driver)
    dash_page.click_header_link('dashboard')
    dash_page.check_image_is_visible()