from pages.base_page import BasePage
from tests.test_group_100000.locators.main_page_locators  import FooterBlockLocators as F
from tests.test_group_100000.locators.main_page_locators import EightDayForecast as D8
from tests.test_group_100000.locators.main_page_locators import MainPageLocators


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
    locators = MainPageLocators()

    def check_manage_cookies_link_is_visible(self):
        manage_cookies_btn = self.element_is_visible(self.locators.MANAGE_COOKIES_BTN)
        assert manage_cookies_btn.is_displayed(), "The Manage cookies module is not visible"
