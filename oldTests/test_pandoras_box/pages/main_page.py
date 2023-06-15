from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    FIELD_WEATHER_IN_YUOR_CITY = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")
    HOME_PAGE = 'https://openweathermap.org/'
    chart_weather = (By.XPATH, "//*[@id='chart-component']")

    def enter_city_in_weather_in_your_city_field(self, city):
        input_city = self.driver.find_element(*self.FIELD_WEATHER_IN_YUOR_CITY)
        input_city.send_keys(city)

    def check_chart_weather_is_displayed(self):
        chart = self.driver.find_element(*self.chart_weather)
        assert chart.is_displayed(), "Chart weather is not visible"

    def check_search_result_contains_city(self, city):
        cities = self.driver.find_elements(*self.result_locator)
        for city_name in cities:
            assert city in city_name.text
