from pages.base_page import BasePage
from locators.locators import WidgetsConstractorLocators
from test_data.all_links import Links


class WidgetsConstructorPage(BasePage):
    locators = WidgetsConstractorLocators()

    def verify_visibility_of_fahrenheit(self):
        url = WidgetsConstructorPage(self.driver, Links.URL_WIDGETS_CONSTRACTOR).open_page()
        fahrenheit = self.driver.find_element(*self.locators.FAHRENHEIT_BUTTON)
        assert fahrenheit.is_displayed()

    def verify_visibility_of_celsius(self):
        widget_page = WidgetsConstructorPage(self.driver, Links.URL_WIDGETS_CONSTRACTOR).open_page()
        celsius = self.driver.find_element(*self.locators.CELSIUS_BUTTON)
        assert celsius.is_displayed()
