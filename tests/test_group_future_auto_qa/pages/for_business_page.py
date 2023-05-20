from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from tests.test_group_future_auto_qa.locators.for_business_page_locators import ForBusinessPageLocators
from pages.base_page import BasePage


class ForBusinessPage(BasePage):
    locators = ForBusinessPageLocators()

    def check_headings(self):
        try:
            for_business = self.element_is_clickable(self.locators.FOR_BUSINESS, 25)
            self.driver.execute_script("arguments[0].click();", for_business)
            self.driver.switch_to.window(self.driver.window_handles[1])
            products = self.element_is_clickable(self.locators.PRODUCTS_IN_HEADER, 20)
            self.driver.execute_script("arguments[0].click();", products)
            return self.elements_are_present(self.locators.PRODUCTS_HEADINGS, 20)
        except TimeoutException:
            return []
