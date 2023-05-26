from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from tests.test_group_future_auto_qa.locators.for_business_page_locators import ForBusinessPageLocators
from pages.base_page import BasePage


class ForBusinessPage(BasePage):
    locators = ForBusinessPageLocators()

    def check_headings(self):
        products = self.element_is_visible(self.locators.PRODUCTS_IN_HEADER, 15)
        products.click()
        headings = self.elements_are_present(self.locators.PRODUCTS_HEADINGS, 15)
        return headings

    def assert_headings_present(self):
        headings = self.check_headings()
        assert len(headings) == 7, "Not all headings are present on the page"

    def check_buttons(self):
        products = self.element_is_visible(self.locators.PRODUCTS_IN_HEADER, 15)
        products.click()
        black_buttons = self.elements_are_present(self.locators.BLACK_BUTTONS, 15)
        orange_buttons = self.elements_are_present(self.locators.ORANGE_BUTTONS, 15)
        if orange_buttons:
            orange_buttons.pop(0)
        buttons = black_buttons + orange_buttons
        return buttons

    def assert_buttons_present(self):
        buttons = self.check_buttons()
        assert len(buttons) == 17, "The count of buttons is not as expected"


