from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import GuidePageLocators
from selenium.webdriver.support.color import Color
from tests.test_group_python_qa.test_data.data_pqa import EXPECTED_LINK_COLOR_HEX


class GuidePage(BasePage):

    locators = GuidePageLocators()

    def link_to_history_archive_is_clickable(self):
        archive_link = self.driver.find_element(*self.locators.LINK_HISTORICAL_ARCHIVE)
        self.action_move_to_element(archive_link)
        assert archive_link.is_enabled(), "The link is not clickable"

    def footer_click_allow(self):
        self.driver.find_element(*self.locators.CLICK_ALLOW_IN_STICK_FOOTER).click()

    def verify_several_links_color(self, locator):
        links = self.driver.find_elements(*locator)
        for link in links:
            link_color_rgba = link.value_of_css_property("color")
            link_color_hex = Color.from_string(link_color_rgba).hex
            assert link_color_hex == EXPECTED_LINK_COLOR_HEX, f"The link color is {link_color_hex}, " \
                                                              f"while {EXPECTED_LINK_COLOR_HEX} is expected"
