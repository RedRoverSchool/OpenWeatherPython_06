from pages.base_page import BasePage
from tests.group_files.the_hardworking_club.locators.locators_all import WeatherDashboardLocators


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
        assert self.driver.current_url == 'https://home.openweathermap.org/questions'

    def verify_weather_dashboard_full_description(self):

        self.driver.get(DashboardPage.url_weather_dashboard)
        dashboard_full_description_text = self.driver.find_element(*self.locators.DASHBOARD_FULL_DESCRIPTION)
        expected_text = "The OpenWeather Dashboard is a lightweight and flexible visual " \
                        "tool for our customers who would like to be notified weather " \
                        "events to make informed decisions and plan actions based on the weather input."
        displayed_text = dashboard_full_description_text.text
        assert expected_text == displayed_text



