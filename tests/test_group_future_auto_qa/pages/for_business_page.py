from tests.test_group_future_auto_qa.locators.for_business_page_locators import ForBusinessPageLocators
from pages.base_page import BasePage


class ForBusinessPage(BasePage):
    locators = ForBusinessPageLocators()

    def check_headings(self):
        for_business = self.element_is_clickable(self.locators.FOR_BUSINESS, 25)
        self.driver.execute_script("arguments[0].click();", for_business)
        self.driver.switch_to.window(self.driver.window_handles[1])
        products = self.element_is_visible(self.locators.PRODUCTS_IN_HEADER, 25)
        products.click()
        headings = self.elements_are_present(self.locators.PRODUCTS_HEADINGS, 25)
        return headings
