from pages.base_page import BasePage
from locators.locators import AccuracyAndQualityOfWeatherDataPageLocators

class AccuracyAndQualityOfWeatherDataPage(BasePage):
    def check_visibility_of_number_of_cities(self):
        number_of_cities = self.driver.find_element(*AccuracyAndQualityOfWeatherDataPageLocators.NUMBER_OF_CITIES_FOR_EVALUATION)
        assert number_of_cities.is_displayed(), 'Number of cities link not found'