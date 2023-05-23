from pages.base_page import BasePage
from tests.test_group_100000.locators.main_page_locators import EightDayForecast as D8


class EightDayForecastPage(BasePage):

    def verify_state_of_sky_in_words_for_each_day_is_displayed(self):
        elements = self.driver.find_elements(*D8.SEARCH_SKY_IN_WORDS)
        for i in elements:
            assert i.is_displayed()

