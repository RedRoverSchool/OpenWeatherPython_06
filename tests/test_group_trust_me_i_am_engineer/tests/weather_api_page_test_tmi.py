from tests.test_group_trust_me_i_am_engineer.pages.weather_api_page import WeatherAPIPage
import pytest

def test_TC_005_04_01_checking_title_page_weather_api(driver):
    page = WeatherAPIPage(driver)
    page.checking_title_page_weather_api()
