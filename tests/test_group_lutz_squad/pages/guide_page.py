from pages.base_page import BasePage
from tests.test_group_lutz_squad.locators.guide_page_locators import GuidePageLocators
from selenium.webdriver.support.color import Color

from tests.test_group_lutz_squad.test_data.data import industry_apis_link_color_hex


class GuidePage(BasePage):

    def industry_apis_link_is_visible_and_clickable(self):
        self.element_is_visible(GuidePageLocators.INDUSTRY_APIS_LOCATOR)
        assert self.element_is_clickable(GuidePageLocators.INDUSTRY_APIS_LOCATOR)

    def industry_check_color(self):
        industry_apis_link_color = Color.from_string(
            self.driver.find_element(*GuidePageLocators.INDUSTRY_APIS_LOCATOR).value_of_css_property(
                'color'))
        assert industry_apis_link_color.hex == industry_apis_link_color_hex
