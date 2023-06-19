from pages.widgets_constructor_page import WidgetsConstructorPage
from locators.locators import WidgetsConstractorLocators


class TestWidgetsConstractorPage:

    def test_tc_001_09_04_verify_visibility_of_fahrenheit(self, driver):
        widget_page = WidgetsConstructorPage(driver)
        widget_page.verify_visibility_of_fahrenheit()

    def test_tc_001_09_03_verify_visibility_of_celsius(self, driver):
        widget_page = WidgetsConstructorPage(driver)
        widget_page.verify_visibility_of_celsius()

    def test_TC_001_09_05_switched_on_Celsius(self, driver):
        widget_page = WidgetsConstructorPage(driver)
        widget_page.check_switched_temperature_units('celsius')

    def test_TC_001_09_06_switched_on_Fahrenheit(self, driver):
        widget_page = WidgetsConstructorPage(driver)
        widget_page.check_switched_temperature_units('fahrenheit')


