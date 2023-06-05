from tests.test_pandoras_box.pages.api_page import ApiPage


def test_005_13_01_check_title_on_page_weather_alert(driver, open_and_load_main_page):
    weather_api = ApiPage(driver)
    weather_api.click_header_link('api')
    weather_api.click_button_api_doc_in_global_weather_alerts()
    weather_api.check_title_features_global_weather_alert()