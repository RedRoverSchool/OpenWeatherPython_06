from pages.base_page import BasePage
from tests.test_group_ducktales.locators.main_locators import MainLocator
from tests.test_group_ducktales.test_data.main_page_data import *
from datetime import datetime


class MainPage(BasePage):

    def get_day_by_weak(self):
        element = self.element_is_visible(MainLocator.FIRST_DAY_IN_8_DAY_FORECAST).text[:3]
        return element

    def day_by_computer(self):
        day_by_computer = datetime.now().weekday()
        today = WEEKDAYS[day_by_computer]
        return today

