from pages.base_page import BasePage
from tests.test_group_lutz_squad.locators.accuracy_and_quality_of_weather_data_page_locators import \
    AccuracyAndQualityOfWeatherDataPageLocators


class AccuracyAndQualityOfWeatherDataPage(BasePage):

    def verify_visibility_of_picture(self, wait):
        accuracy_and_quality_of_weather_data_page = self.driver.find_element(
            *AccuracyAndQualityOfWeatherDataPageLocators.accuracy_and_quality_of_weather_data_link_locator)
        self.go_to_element(accuracy_and_quality_of_weather_data_page)
        accuracy_and_quality_of_weather_data_page.click()
        assert self.driver.current_url == 'https://openweathermap.org/accuracy-and-quality'
        example_of_graphics_with_some_metrics = self.driver.find_element(
            *AccuracyAndQualityOfWeatherDataPageLocators.example_of_graphics_with_some_metrics_locator)
        self.go_to_element(example_of_graphics_with_some_metrics)
        assert self.element_is_displayed(AccuracyAndQualityOfWeatherDataPageLocators.example_of_graphics_with_some_metrics_locator, wait)

