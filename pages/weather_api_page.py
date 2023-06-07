from pages.base_page import BasePage
from locators.locators import ClimateForecastLocators as CF


class WeatherApiPage(BasePage):
    def check_visibility_climatic_forecast_30_days_page_title(self):
        title_page = self.driver.find_element(*CF.TITLE_FORCAST30).text
        assert title_page == 'Climate forecast for 30 days', 'The title of the page does not match the expected value'

    def check_redirect_to_the_how_to_make_of_the_page(self):
        self.find_element_and_click(CF.LINK_HOW_TO_MAKE)
        new_page_title = self.driver.find_element(*CF.TITLE_HOW_TO_MAKE)
        assert new_page_title.is_displayed(), 'The title of the page does not match the expected value'
