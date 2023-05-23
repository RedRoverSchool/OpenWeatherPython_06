import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from tests.test_the_hardworking_club.locators.locators_all import WeatherDashboardLocators


class DashboardPage(BasePage):

    url_weather_dashboard = 'https://openweathermap.org/weather-dashboard'
    locators = WeatherDashboardLocators()

    def verify_the_button_Contact_Us_works(self):

        self.driver.get(DashboardPage.url_weather_dashboard)
        my_CONTACT_US = self.driver.find_element(*self.locators.CONTACT_US)
        assert my_CONTACT_US.is_enabled()



