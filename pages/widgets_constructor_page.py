from pages.base_page import BasePage
from locators.locators import WidgetsConstractorLocators
from test_data.all_links import Links
from selenium.webdriver.common.action_chains import ActionChains

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

    def check_switched_temperature_units(self, temperature_units):
        widget_page = WidgetsConstructorPage(self.driver, Links.URL_WIDGETS_CONSTRACTOR).open_page()
        expected_position = 'color: rgb(235, 110, 75);'
        match temperature_units:
            case 'celsius':
                toggle_position = self.driver.find_element(*self.locators.CELSIUS_BUTTON)
                if toggle_position.get_attribute("style") == expected_position:
                    action = ActionChains(self.driver)
                    action.double_click(toggle_position).perform()
                    for widget_locator in self.locators.widgets_locators:
                        self.element_is_visible(widget_locator)
                    metric_units_number = self.driver.find_elements(*self.locators.metric_units)
                    assert len(metric_units_number) == 14, "Units did not switch correctly"
                else:
                    self.driver.find_element(*self.locators.metric_toggle).click()
                    for widget_locator in self.locators.widgets_locators:
                        self.element_is_visible(widget_locator)
                    metric_units_number = self.driver.find_elements(*self.locators.metric_units)
                    assert len(metric_units_number) == 14, "Units did not switch correctly"
            case 'fahrenheit':
                toggle_position = self.driver.find_element(*self.locators.CELSIUS_BUTTON)
                if toggle_position.get_attribute("style") == expected_position:
                    self.driver.find_element(*self.locators.CELSIUS_BUTTON).click()
                    for widget_locator in self.locators.widgets_locators:
                        self.element_is_visible(widget_locator)
                    imperial_units_number = self.driver.find_elements(*self.locators.imperial_units)
                    assert len(imperial_units_number) == 14, "Units did not switch correctly"
                else:
                    action = ActionChains(self.driver)
                    action.double_click(toggle_position).perform()
                    for widget_locator in self.locators.widgets_locators:
                        self.element_is_visible(widget_locator)
                    imperial_units_number = self.driver.find_elements(*self.locators.imperial_units)
                    assert len(imperial_units_number) == 14, "Units did not switch correctly"