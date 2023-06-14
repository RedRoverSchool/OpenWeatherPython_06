from locators.locators import WeatherConditionsLocators
from pages.weather_conditions_page import WeatherConditionsPage
from test_data.urls import WeatherConditionsUrls
from test_data.weather_conditions_page_data import WeatherConditionsData as data
import pytest


class TestWeatherConditions:

    def test_tc_001_10_03_verify_count_of_icons_for_night_time(self, driver):
        weather_conditions_page = WeatherConditionsPage(driver, WeatherConditionsUrls.url_weather_conditions)
        weather_conditions_page.open_page()
        weather_conditions_page.find_element_and_click(WeatherConditionsLocators.WEATHER_ICONS)
        weather_conditions_page.verify_count_of_icons_for_night_time(driver)

    @pytest.mark.parametrize('table', data.TABLES)
    def test_tc_001_12_07_verify_that_codes_and_descriptions_are_visible_for_each_weather_condition_group_part1(self, driver, table):
        weather_conditions_page = WeatherConditionsPage(driver, WeatherConditionsUrls.url_weather_conditions)
        weather_conditions_page.open_page()
        weather_conditions_page.check_codes_are_visible(driver, table)

    @pytest.mark.parametrize('table', data.TABLES)
    def test_tc_001_12_07_verify_that_codes_and_descriptions_are_visible_for_each_weather_condition_group_part2(self, driver, table):
        weather_conditions_page = WeatherConditionsPage(driver, WeatherConditionsUrls.url_weather_conditions)
        weather_conditions_page.open_page()
        weather_conditions_page.check_desc_are_visible(driver, table)