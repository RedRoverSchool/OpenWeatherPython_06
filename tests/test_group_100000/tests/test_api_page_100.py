from tests.test_group_100000.pages.api_page import *
from tests.test_group_100000.pages.api_page import OneCallApiPage
from tests.test_group_100000.locators.api_page_locators import WeatherConditions as W
from tests.test_group_100000.locators.api_page_locators import OneCallApi as O


class TestWeatherConditions:
    def test_RF_AT_001_12_04_Drizzle_group_of_codes_visible(self, driver):
        page = WeatherConditionsPage(driver, link=W.CONDITION_URL)
        page.open_page()
        page.check_visibility_drizzle_group()


class TestOneCallApi:
    def test_008_02_04_verify_redirection_One_Call_API_3_link(self, driver):
        page = OneCallApiPage(driver, link=O.API_PAGE)
        page.open_page()
        page.verify_redirection_one_call_api_3_link()


class TestCopyrightBlock:
    def test_TC_003_11_02_verify_the_copyright_information_is_present_on_the_site_page(self, driver):
        page = FooterApiPage(driver, link=O.API_PAGE)
        page.open_page()
        page.verify_the_copyright_information_is_present_on_the_site_page()
