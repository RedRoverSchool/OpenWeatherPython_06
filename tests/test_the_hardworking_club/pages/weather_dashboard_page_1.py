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

    def button_leads_to_the_correct_page(self):

        self.driver.get(DashboardPage.url_weather_dashboard)
        my_CONTACT_US = self.driver.find_element(*self.locators.CONTACT_US)
        my_FOOTER_PANEL = self.driver.find_element(*self.locators.FOOTER_PANEL).click()
        my_CONTACT_US.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == 'https://home.openweathermap.org/questions' "URL is not correct!."



