from pages.base_page import BasePage
from tests.test_group_lutz_squad.locators.guide_page_locators import GuidePageLocators
from selenium.webdriver.support.color import Color

from tests.test_group_lutz_squad.test_data.data import industry_apis_link_color_hex
from tests.test_group_lutz_squad.locators.links import API_PAGE_LINK
from tests.test_group_lutz_squad.locators.links import ONE_CALL_3_LINK


class GuidePage(BasePage):

    def industry_apis_link_is_visible_and_clickable(self):
        self.element_is_visible(GuidePageLocators.INDUSTRY_APIS_LOCATOR)
        assert self.element_is_clickable(GuidePageLocators.INDUSTRY_APIS_LOCATOR)

    def industry_check_color(self):
        industry_apis_link_color = Color.from_string(
            self.driver.find_element(*GuidePageLocators.INDUSTRY_APIS_LOCATOR).value_of_css_property(
                'color'))
        assert industry_apis_link_color.hex == industry_apis_link_color_hex

    def industry_standard_apis_link_redirection(self):
        element = self.driver.find_element(*GuidePageLocators.INDUSTRY_APIS_LOCATOR)
        self.driver.execute_script("arguments[0].click();", element)
        expected_link = API_PAGE_LINK
        assert self.driver.current_url == expected_link, "This link is not correct"



    def one_call_api_by_call_link_redirection(self):
        element = self.driver.find_element(*GuidePageLocators.ONE_CALL_API_BY_CALL_LOCATOR)
        self.driver.execute_script("arguments[0].click();", element)
        expected_link = ONE_CALL_3_LINK
        assert self.driver.current_url == expected_link, "This link is not correct"

