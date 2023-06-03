from tests.test_group_bugs_in_each_step.pages.main_page import MainPage
from tests.test_group_bugs_in_each_step.test_data.urls import MainPageUrls
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestHistoricalWeatherDataLink:

    def test_tc_003_03_03_historical_weather_data_link_visibility(self, driver):
        historical_weather_data_link = MainPage(driver, MainPageUrls.url_main_page)
        historical_weather_data_link.open_page()
        element = historical_weather_data_link.check_historical_weather_data_link_is_visible()
        assert element is True, 'The element is not visible'

    def test_tc_003_12_01_check_historical_weather_data_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_historical_weather_data_link_functionality()


class TestFooterLinksFunctionality:
    def test_TC_003_12_04_current_and_forecast_apis_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_current_and_forecast_apis_functionality()


class TestFooterLinksclickability:
    def test_TC_003_03_02_verify_clickability_current_and_forecast_apis(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_clickability_current_and_forecast_apis()


class TestHowToStartLink:
    def test_tc_003_05_02_verify_how_to_start_visibility(self, driver, open_and_load_main_page, wait):
        page = MainPage(driver)
        page.verify_how_to_start_visibility()

    def test_tc_003_12_18_verify_how_to_start_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_how_to_start_link_functionality()


class TestWeatherMapsLink:
    def test_tc_003_12_03_verify_weather_maps_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_maps_link_functionality()


class TestWeatherDashboardLink:
    def test_tc_003_03_04_verify_weather_dashboard_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_is_visible()

    def test_tc_003_03_05_verify_weather_dashboard_link_clickability(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_is_clickable()

    def test_tc_003_12_02_verify_weather_data_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_functionality()


class TestOurTechnologyLink:
    def test_tc_003_12_08_verify_our_technology_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_our_technology_link_functionality()


class TestAccuracyAndQualityOfWeatherDataLink:
    def test_tc_003_12_16_verify_accuracy_and_quality_of_weather_data_link_functionality\
                    (self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_accuracy_and_quality_of_weather_data_link_functionality()


class TestConnectYourWeatherStationLink:
    def test_tc_003_12_17_verify_connect_your_weather_station_link_functionality\
                    (self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_connect_your_weather_station_link_functionality()

class TestSubscribeForFreeLink:
    def test_tc_003_12_19_verify_subscribe_for_free_link_functionality_for_unauthorized_user\
                    (self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_subscribe_for_free_link_functionality()

class TestWebsiteTermsAndConditionsLink:
        def test_tc_003_06_03_verify_website_terms_and_conditions_link_visibility\
                        (self, driver,open_and_load_main_page):
            page = MainPage(driver)
            page.check_website_terms_and_conditions_link_visibility()


class TestOpenWeatherForBusinessLink:
    def test_tc_003_12_21_verify_openweather_for_business_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        expected_link = "https://openweather.co.uk/"
        page.check_openweather_for_business_link_functionality(expected_link)
