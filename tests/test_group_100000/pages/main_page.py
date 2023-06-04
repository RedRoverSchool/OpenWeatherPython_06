from pages.base_page import BasePage
from tests.test_group_100000.locators.main_page_locators import FooterBlockLocators as F, MainPageLocators
from tests.test_group_100000.locators.main_page_locators import EightDayForecast as D8


class FooterBlock(BasePage):
    def verify_how_to_start_link_is_clickable(self):
        how_to_start = self.driver.find_element(*F.HOW_TO_START_LINK)
        assert how_to_start.is_enabled(), "The 'How to start' link does not clickable"


class EightDayForecastPage(BasePage):
    def verify_state_of_sky_in_words_for_each_day_is_displayed(self):
        elements = self.driver.find_elements(*D8.SEARCH_SKY_IN_WORDS)
        for i in elements:
            assert i.is_displayed()
class MainPage(BasePage):
    URL = 'https://openweathermap.org/'
    locators = MainPageLocators()

    def go_to_about_us_page(self):
        self.element_is_clickable(self.locators.ABOUT_US_BUTTON).click()

