from pages.base_page import BasePage
from oldTests.test_group_optimists_of_rationality_middle_devs.locators.for_business_page_locators import ForBusinessPageLocators

class ForBusinessPage(BasePage):
    locators = ForBusinessPageLocators()


    def assert_elements_are_clickable(self):
        clickable_elements = self.check_elements_are_clickable()
        assert all(clickable_elements), "Not all elements are clickable"

    def check_elements(self):
        talk_to_us_button = self.element_is_present(self.locators.TALK_TO_US_BUTTON)
        current_and_forecasts = self.element_is_present(self.locators.CURRENT_AND_FORECASTS)
        historical_data = self.element_is_present(self.locators.HISTORICAL_DATA)
        weather_alerts = self.element_is_present(self.locators.WEATHER_ALERTS)
        weather_maps = self.element_is_present(self.locators.WEATHER_MAPS)
        energy_prediction = self.element_is_present(self.locators.ENERGY_PREDICTION)
        return [talk_to_us_button, current_and_forecasts, historical_data, weather_alerts, weather_maps,
                energy_prediction]

    def check_elements_are_clickable(self):
        elements = self.check_elements()
        return [element.is_enabled() for element in elements]


