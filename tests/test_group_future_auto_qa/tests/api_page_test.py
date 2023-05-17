from tests.test_group_future_auto_qa.pages.api_page import *
import pytest


class TestTitle:
    def test_TC_005_10_01_visibility_of_weather_api_page_title(self, driver):
        api_page = ApiPage(driver, "https://openweathermap.org/api")
        api_page.open_page()
        assert driver.title == 'Weather API - OpenWeatherMap', "The title of the page is incorrect"



