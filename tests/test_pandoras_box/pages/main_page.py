from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    FIELD_WEATHER_IN_YUOR_CITY = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")
    HOME_PAGE = 'https://openweathermap.org/'

    def enter_city_in_weather_in_your_city_field(self, city):
        input_city = self.driver.find_element(*self.FIELD_WEATHER_IN_YUOR_CITY)
        input_city.send_keys(city)