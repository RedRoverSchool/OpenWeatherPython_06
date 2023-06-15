from oldTests.test_group_zmeyki.locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators()

    def graphic_hourly_forecast_is_displayed(self, wait):
        graphic_hourly_forecast = self.driver.find_element(*self.locators.graphic_hourly_forecast_locator)
        self.go_to_element(graphic_hourly_forecast)
        assert self.element_is_visible

    def weather_items_are_displayed(self, wait):
        self.driver.get(self.locators.URL)
        weather_items = self.driver.find_elements(*self.locators.weather_items_locator)
        self.driver.execute_script("arguments[0].scrolldown;", weather_items)
        assert self.weather_items_are_displayed


