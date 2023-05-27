from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from tests.test_group_future_auto_qa.locators.for_business_page_locators import ForBusinessPageLocators
from pages.base_page import BasePage


class ForBusinessPage(BasePage):
    locators = ForBusinessPageLocators()

    def check_headings(self):
        products = self.element_is_visible(self.locators.PRODUCTS_IN_HEADER, 15)
        products.click()
        headings = self.elements_are_present(self.locators.PRODUCTS_HEADINGS, 15)
        return headings

    def assert_headings_present(self):
        headings = self.check_headings()
        assert len(headings) == 7, "Not all headings are present on the page"

    def check_buttons(self):
        products = self.element_is_visible(self.locators.PRODUCTS_IN_HEADER)
        products.click()
        black_buttons = self.elements_are_present(self.locators.BLACK_BUTTONS)
        orange_buttons = self.elements_are_present(self.locators.ORANGE_BUTTONS)
        if orange_buttons:
            orange_buttons.pop(0)
        buttons = black_buttons + orange_buttons
        return buttons

    def assert_buttons_present(self):
        buttons = self.check_buttons()
        assert len(buttons) == 17, "The count of buttons is not as expected"

    def check_elements(self):
        talk_to_us_button = self.element_is_present(self.locators.TALK_TO_US_BUTTON)
        current_and_forecasts = self.element_is_present(self.locators.CURRENT_AND_FORECASTS)
        historical_data = self.element_is_present(self.locators.HISTORICAL_DATA)
        weather_alerts = self.element_is_present(self.locators.WEATHER_ALERTS)
        weather_maps = self.element_is_present(self.locators.WEATHER_MAPS)
        energy_prediction = self.element_is_present(self.locators.ENERGY_PREDICTION)
        return [talk_to_us_button, current_and_forecasts, historical_data, weather_alerts, weather_maps,
                energy_prediction]

    def assert_elements_present(self):
        elements = self.check_elements()
        assert all(elements), "Not all elements are present on the page"

