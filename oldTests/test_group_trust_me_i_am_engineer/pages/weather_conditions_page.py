from pages.base_page import BasePage
from oldTests.test_group_trust_me_i_am_engineer.locators.page_locators import WeatherConditionsLocators

class WeatherConditionsPage(BasePage):
    URL_WEATHER_CONDITIONS = 'https://openweathermap.org/weather-conditions'
    locators = WeatherConditionsLocators()

    def weather_conditions_verify_list_of_description(self):
        expected_list_description = ['clear sky', 'few clouds', 'scattered clouds', 'broken clouds', 'rain', 'snow']
        self.driver.get(self.URL_WEATHER_CONDITIONS)
        list_description = self.driver.find_elements(*self.locators.ICON_LIST_DESCRIPTION)
        actual_list_description = [el.text for el in list_description]
        difference = set(expected_list_description) - set(actual_list_description)
        assert len(difference) == 0
