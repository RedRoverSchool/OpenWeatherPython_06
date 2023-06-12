from tests.test_group_100000.pages.api_page import *
from tests.test_group_100000.pages.api_page import OneCallApiPage, WeatherConditionsPage
from tests.test_group_100000.locators.api_page_locators import WeatherConditions as W
from tests.test_group_100000.locators.api_page_locators import OneCallApi as O


class TestWeatherConditions:
    def test_RF_AT_001_12_04_Drizzle_group_of_codes_visible(self, driver):
        page = WeatherConditionsPage(driver, link=W.CONDITION_URL)
        page.open_page()
        page.check_visibility_drizzle_group()

    def test_RF_TC_001_12_06_Verify_that_drizzel_group_of_codes_contains_more_than_1_item(self, driver):
        page = WeatherConditionsPage(driver, link=W.CONDITION_URL)
        page.open_page()
        page.verify_that_drizzle_group_of_codes_contains_more_than_1_item()


class TestOneCallApi:
    def test_008_02_04_verify_redirection_One_Call_API_3_link(self, driver):
        page = OneCallApiPage(driver, link=O.API_PAGE)
        page.open_page()
        page.verify_redirection_one_call_api_3_link()


class TestCopyrightBlock:
    def test_TC_003_11_02_verify_the_copyright_information_is_present_on_the_site_page(self, driver):
        page = FooterApiPage(driver, O.API_PAGE)
        page.open_page()
        page.verify_the_copyright_information_is_present_on_the_site_page()


class TestClimaticForecast30:
    def test_TC_005_06_1_visibility_climatic_forecast_30_days_page_title(self, driver):
        page = ClimaticForecast(driver, ClimateForecast.URL_FORCAST30)
        page.open_page()
        page.check_visibility_climatic_forecast_30_days_page_title()

    def test_TC_005_06_02_redirect_to_the_how_to_make_an_api_call_section_of_the_page(self, driver):
        page = ClimaticForecast(driver, ClimateForecast.URL_FORCAST30)
        page.open_page()
        page.check_redirect_to_the_how_to_make_of_the_page()
