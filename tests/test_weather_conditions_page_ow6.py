from locators.locators import WeatherConditionsLocators
from pages.weather_conditions_page import WeatherConditionsPage
from test_data.urls import WeatherConditionsUrls


class TestWeatherConditions:

    def test_tc_001_10_03_verify_count_of_icons_for_night_time(self, driver):
        weather_conditions_page = WeatherConditionsPage(driver, WeatherConditionsUrls.url_weather_conditions)
        weather_conditions_page.open_page()
        weather_conditions_page.find_element_and_click(WeatherConditionsLocators.WEATHER_ICONS)
        weather_conditions_page.verify_count_of_icons_for_night_time(driver)
