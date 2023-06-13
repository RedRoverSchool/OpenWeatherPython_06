from pages.base_page import BasePage
from oldTests.test_group_snake_oil.locators.pricing_for_business_locators import PricingForBusinessLocators


class PricingForBusinessPage(BasePage):
    locators = PricingForBusinessLocators

    def get_table_content(self):
        table = self.element_is_visible(self.locators.TABLE)
        print(type(table.text))
