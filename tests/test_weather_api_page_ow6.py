from pages.weather_api_page import WeatherApiPage
from locators.locators import ClimateForecastLocators as CFL
from pages.api_page import APIPage
from test_data.urls import ApiPageUrls


class TestWeatherApiPage:
    def test_tc_005_06_1_visibility_climatic_forecast_30_days_page_title(self, driver):
        page = WeatherApiPage(driver, CFL.URL_FORCAST30)
        page.open_page()
        page.check_visibility_climatic_forecast_30_days_page_title()

    def test_tc_005_06_02_redirect_to_the_how_to_make_an_api_call_section_of_the_page(self, driver):
        page = WeatherApiPage(driver, CFL.URL_FORCAST30)
        page.open_page()
        page.check_redirect_to_the_how_to_make_of_the_page()

    def test_005_13_01_check_title_on_page_weather_alert(self, driver, open_and_load_main_page):
        weather_api = APIPage(driver)
        weather_api.click_header_link('api')
        weather_api.click_button_api_doc_in_global_weather_alerts()
        weather_api.check_title_features_global_weather_alert()

    def test_005_17_01_check_title_history_api_full_archive(self, driver, open_and_load_main_page):
        history_api_full = APIPage(driver)
        history_api_full.click_header_link('api')
        history_api_full.click_button_api_doc_history_full_archive()
        history_api_full.check_title_history_api_full_archive()


    def test_005_17_02_check_api_calls_and_responses(self, driver):
        history_api_full = APIPage(driver, ApiPageUrls.HISTORY_API_FULL_ARCHIVE_LINK)
        history_api_full.open_page()
        history_api_full.verify_present_api_calls_and_responses()



    def test_tc_005_13_02_check_visibility_button_get_access(self, driver):
        weather_api = APIPage(driver, link=ApiPageUrls.GLOBAL_WEATHER_ALERTS_LINK)
        weather_api.open_page()
        weather_api.verify_visibility_button_get_access()

    def test_tc_005_13_03_check_redirection_page_get_access(self, driver):
        weather_api = APIPage(driver, link=ApiPageUrls.GLOBAL_WEATHER_ALERTS_LINK)
        weather_api.open_page()
        weather_api.verify_get_access_redirects_to_valid_page()


    def test_tc_005_17_03_check_5_headers(self, driver):
        weather_api = APIPage(driver, link=ApiPageUrls.GLOBAL_WEATHER_ALERTS_LINK)
        weather_api.open_page()
        weather_api.verify_five_headers_are_present()

