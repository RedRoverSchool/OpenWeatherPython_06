from pages.base_page import BasePage
from locators.locators import MapsPageLocators

class MapsPage(BasePage):
    def cities_checkbox_is_checked(self):
        cities_checkbox = self.driver.find_element(*MapsPageLocators.CITIES_CHECKBOX_INPUT)
        assert cities_checkbox.is_selected()

    def cities_checkbox_is_unchecked(self):
        self.driver.find_element(*MapsPageLocators.CITIES_CHECKBOX_LABEL).click()
        cities_checkbox_input = self.driver.find_element(*MapsPageLocators.CITIES_CHECKBOX_INPUT)
        assert not cities_checkbox_input.is_selected()