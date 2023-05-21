from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WeatherDashboard(BasePage):

    dashboard_URL = 'https://openweathermap.org/weather-dashboard'
    pricing_plans_locators = [(By.XPATH, '//h4[text()="Free"]'),
                              (By.XPATH, '//h4[text()="Startup"]'),
                              (By.XPATH, '//h4[text()="Developer"]'),
                              (By.XPATH, '//h4[text()="Professional"]'),
                              (By.XPATH, '//h4[text()="Enterprise"]')]

    def check_pricing_plans(self):
        for plan_locator in self.pricing_plans_locators:
            plan = self.driver.find_element(*plan_locator)
            assert plan.is_displayed()