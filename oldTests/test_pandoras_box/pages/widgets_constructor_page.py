from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
class WidgetsConstructor(BasePage):

    widget_constructor_URL = 'https://openweathermap.org/widgets-constructor'
    metric_toggle = (By.XPATH, '//span[@id="metric"]')
    metric_units = (By.XPATH, '//span[text()="°C"]')
    imperial_units = (By.XPATH, '//span[text()="°F"]')
    widgets_locators = [(By.XPATH, '//*[@id="container-openweathermap-widget-11"]'),
                        (By.XPATH, '//*[@id="container-openweathermap-widget-12"]'),
                        (By.XPATH, '//*[@id="container-openweathermap-widget-13"]'),
                        (By.XPATH, '//*[@id="container-openweathermap-widget-14"]'),
                        (By.XPATH, '//*[@id="container-openweathermap-widget-15"]'),
                        (By.XPATH, '//*[@id="container-openweathermap-widget-16"]'),
                        (By.XPATH, '//*[@id="container-openweathermap-widget-17"]'),
                        (By.XPATH, '//*[@id="container-openweathermap-widget-18"]'),
                        (By.XPATH, '//*[@id="container-openweathermap-widget-19"]')]

    def check_switched_temperature_units(self, temperature_units):
        expected_position = 'color: rgb(235, 110, 75);'
        match temperature_units:
            case 'celsius':
                toggle_position = self.driver.find_element(*self.metric_toggle)
                if toggle_position.get_attribute("style") == expected_position:
                    action = ActionChains(self.driver)
                    action.double_click(toggle_position).perform()
                    for widget_locator in self.widgets_locators:
                        self.element_is_visible(widget_locator)
                    metric_units_number = self.driver.find_elements(*self.metric_units)
                    assert len(metric_units_number) == 14, "Units did not switch correctly"
                else:
                    self.driver.find_element(*self.metric_toggle).click()
                    for widget_locator in self.widgets_locators:
                        self.element_is_visible(widget_locator)
                    metric_units_number = self.driver.find_elements(*self.metric_units)
                    assert len(metric_units_number) == 14, "Units did not switch correctly"
            case 'fahrenheit':
                toggle_position = self.driver.find_element(*self.metric_toggle)
                if toggle_position.get_attribute("style") == expected_position:
                    self.driver.find_element(*self.metric_toggle).click()
                    for widget_locator in self.widgets_locators:
                        self.element_is_visible(widget_locator)
                    imperial_units_number = self.driver.find_elements(*self.imperial_units)
                    assert len(imperial_units_number) == 14, "Units did not switch correctly"
                else:
                    action = ActionChains(self.driver)
                    action.double_click(toggle_position).perform()
                    for widget_locator in self.widgets_locators:
                        self.element_is_visible(widget_locator)
                    imperial_units_number = self.driver.find_elements(*self.imperial_units)
                    assert len(imperial_units_number) == 14, "Units did not switch correctly"