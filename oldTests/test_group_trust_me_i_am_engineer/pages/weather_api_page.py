from pages.base_page import BasePage
from oldTests.test_group_trust_me_i_am_engineer.locators.page_locators import WeatherAPIPageLocators

class WeatherAPIPage(BasePage):
    URL_WEATHER_API = 'https://openweathermap.org/api'
    locators = WeatherAPIPageLocators()

    def checking_title_page_weather_api(self):
        expected_weather_api_page_title = "Weather API"
        self.driver.get(self.URL_WEATHER_API)
        page_title = self.driver.find_element(*self.locators.WEATHER_API_PAGE_TITLE)
        assert expected_weather_api_page_title == page_title.text, \
            "The title of the Weather API page does not match the expected title"