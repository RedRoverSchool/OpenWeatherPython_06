from pages.base_page import BasePage
from tests.test_group_lutz_squad.locators.accuracy_and_quality_of_weather_data_page_locators import \
    AccuracyAndQualityOfWeatherDataPageLocators


class AccuracyAndQualityOfWeatherDataPage(BasePage):

    def verify_visibility_of_picture(self, wait):
        accuracy_and_quality_of_weather_data_page = self.driver.find_element(
            *AccuracyAndQualityOfWeatherDataPageLocators.ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK_LOCATOR)
        self.go_to_element(accuracy_and_quality_of_weather_data_page)
        accuracy_and_quality_of_weather_data_page.click()
        example_of_graphics_with_some_metrics = self.driver.find_element(
            *AccuracyAndQualityOfWeatherDataPageLocators.EXAMPLE_OF_GRAPHICS_WITH_SOME_METRICS_LOCATOR)
        self.go_to_element(example_of_graphics_with_some_metrics)
        assert self.element_is_displayed(AccuracyAndQualityOfWeatherDataPageLocators.EXAMPLE_OF_GRAPHICS_WITH_SOME_METRICS_LOCATOR, wait)


    def check_visibility_of_number_of_cities(self):
        number_of_cities = self.driver.find_element(*AccuracyAndQualityOfWeatherDataPageLocators.number_of_cities_for_evaluation)
        assert number_of_cities.is_displayed(), 'Number of cities link not found'
