from pages.base_page import BasePage
from tests.test_group_100000.locators.main_page_locators import AboutUsPageLocators

class AboutUsPage(BasePage):
    URL = "https://openweathermap.org/about-us"
    page_locators = AboutUsPageLocators

    def open(self):
        self.driver.get(self.URL)

    def verify_correct_header_about_us_page(self):
        self.element_is_visible(self.page_locators.HEADER)

        assert self.element_is_visible(self.page_locators.HEADER).text == "OpenWeather\nglobal services"