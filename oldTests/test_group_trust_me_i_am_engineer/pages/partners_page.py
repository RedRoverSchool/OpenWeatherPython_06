import time

from selenium.webdriver.support import expected_conditions as EC
from pages import base_page
from pages.base_page import BasePage
from oldTests.test_group_trust_me_i_am_engineer.locators.page_locators import PartnersPageLocators

class PartnersPage(BasePage):
    URL_PARTNERS = 'https://openweathermap.org/examples'
    locators = PartnersPageLocators()
    drupal_button = 'https://www.drupal.org/project/olowm'
    awesome_widget_button = 'http://wordpress.org/extend/plugins/awesome-weather/'
    repositories_openweather = 'https://github.com/search?q=openweathermap&ref=cmdform&type=repositories'

    def verify_the_link_view_on_github_is_visible(self):
        self.driver.get(self.URL_PARTNERS)
        button = self.driver.find_element(*self.locators.BUTTON_VIEW_ON_GITHUB)
        self.go_to_element(button)
        assert button.is_displayed(), \
            "The 'View on Github' button is not displayed"

    def verify_redirection_drupal_button_leads_to_the_new_website(self):
        self.driver.get(self.URL_PARTNERS)
        button = self.driver.find_element(*self.locators.BUTTON_SEE_ON_THE_WEBSITE)
        self.driver.execute_script("arguments[0].click();", button)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.drupal_button, self.driver.current_url

    def verify_the_link_view_on_github_is_clickable(self):
        self.driver.get(self.URL_PARTNERS)
        button = self.driver.find_element(*self.locators.BUTTON_VIEW_ON_GITHUB)
        self.go_to_element(button)
        assert button.is_enabled(), \
            "The 'View on Github' button is not clickable"

    def verify_the_link_open_manual_is_visible(self):
        self.driver.get(self.URL_PARTNERS)
        button = self.driver.find_element(*self.locators.BUTTON_OPEN_MANUAL)
        self.go_to_element(button)
        assert button.is_displayed(), \
            "The 'Open manual' button is not displayed"

    def verify_the_link_open_manual_is_clickable(self):
        self.driver.get(self.URL_PARTNERS)
        button = self.driver.find_element(*self.locators.BUTTON_OPEN_MANUAL)
        self.go_to_element(button)
        assert button.is_enabled(), \
            "The 'Open manual' button is not clickable"

    def verify_17_sections_are_visible(self):
        data = ["Google Weather-Based Campaign Management with OpenWeatherMap API",
                "Google Maps JavaScript API based on OpenWeatherMap API",
                "OpenWeather current weather data in Mozilla's IoT project",
                "Ubuntu", "Android", "Leaflet", "Java", "Go (golang)",
                "JavaScript", "CMS", "Raspberry Pi", "Python", "PHP", "Apache Camel",
                "Desktop", "Mobile applications", "6,000+ repositories on GitHub"]
        self.driver.get(self.URL_PARTNERS)
        find_all_headers = self.driver.find_elements(*self.locators.HEADERS_ON_THE_PAGE)
        headers_on_the_page = [i.text for i in find_all_headers]
        assert data == headers_on_the_page

    def verify_wordpress_awesome_weather_widget_leads_to_the_new_website(self):
        self.driver.get(self.URL_PARTNERS)
        awesome_button = self.driver.find_element(*self.locators.BUTTON_VIEW_WIDGET)
        self.driver.execute_script("arguments[0].click();", awesome_button)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        assert self.awesome_widget_button, self.driver.current_url

    def verify_the_link_view_solutions_leads_to_the_new_website(self):
        self.driver.get(self.URL_PARTNERS)
        view_solutions_button = self.driver.find_element(*self.locators.BUTTON_VIEW_SOLUTIONS)
        self.driver.execute_script("arguments[0].click();", view_solutions_button)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(4)
        assert self.repositories_openweather, self.driver.current_url

