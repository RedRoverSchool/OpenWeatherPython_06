from pages.widgets_constructor_page import WidgetsConstructorPage
from locators.locators import WidgetsConstractorLocators


class TestWidgetsConstractorPage:

    def test_tc_001_09_04_verify_visibility_of_fahrenheit(self, driver):
        widget_page = WidgetsConstructorPage(driver)
        widget_page.verify_visibility_of_fahrenheit()







