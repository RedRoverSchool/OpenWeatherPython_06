from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class WeatherConditions(BasePage):

    condition_URL = 'https://openweathermap.org/weather-conditions'
    thunderstorm_locator = (By.XPATH, '//a[contains(@href, "#Thunderstorm")]/ancestor-or-self::table//tr')

    def check_number_of_elements(self, group_locator):
        match group_locator:
            case 'thunderstorm':
                codes_number = self.driver.find_elements(*self.thunderstorm_locator)
                assert len(codes_number) >= 3, "The number of elements is not as expected"