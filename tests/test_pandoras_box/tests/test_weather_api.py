from tests.test_pandoras_box.pages.api_page import APIPage


def test_005_17_01_check_title_history_api_full_archive(driver, open_and_load_main_page):
    history_api_full = APIPage(driver)
    history_api_full.click_header_link('api')
    history_api_full.click_button_api_doc_history_full_archive()
    history_api_full.check_title_history_api_full_archive()


def test_005_13_01_check_title_on_page_weather_alert(driver, open_and_load_main_page):
    weather_api = APIPage(driver)
    weather_api.click_header_link('api')
    weather_api.click_button_api_doc_in_global_weather_alerts()
    weather_api.check_title_features_global_weather_alert()
