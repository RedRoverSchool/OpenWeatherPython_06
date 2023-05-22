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


class TestFooterLinksFunctionality:
    def test_TC_003_12_04_current_and_forecast_apis_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_current_and_forecast_apis_functionality()

class TestFooterLinksclickability:
    def test_TC_003_03_02_verify_clickability_current_and_forecast_apis(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_clickability_current_and_forecast_apis()
