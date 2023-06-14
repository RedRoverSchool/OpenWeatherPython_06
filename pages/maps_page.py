from pages.base_page import BasePage
from locators.locators import MapsPageLocators
from locators.locators import BasePageLocators
from test_data.urls import SuitsUrls

class MapsPage(BasePage):
    def cities_checkbox_is_checked(self):
        cities_checkbox = self.driver.find_element(*MapsPageLocators.CITIES_CHECKBOX_INPUT)
        assert cities_checkbox.is_selected()

    def cities_checkbox_is_unchecked(self):
        self.driver.find_element(*MapsPageLocators.CITIES_CHECKBOX_LABEL).click()
        cities_checkbox_input = self.driver.find_element(*MapsPageLocators.CITIES_CHECKBOX_INPUT)
        assert not cities_checkbox_input.is_selected()

    def check_open_maps(self, link_name):
        self.click_header_link(link_name)
        assert '/weathermap' in self.driver.current_url

    def check_return_main(self):
        self.driver.find_element(*BasePageLocators.LOGO_LOCATOR).click()
        assert self.driver.current_url == SuitsUrls.URLs[0]
