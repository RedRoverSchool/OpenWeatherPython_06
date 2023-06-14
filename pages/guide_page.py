from pages.base_page import BasePage
from locators.locators import GuideLocators
from selenium.webdriver.support.color import Color
from test_data.miscellaneous import BasePageMisc


class GuidePage(BasePage):

    guide_locators = GuideLocators()

    def link_to_history_archive_is_clickable(self):
        archive_link = self.driver.find_element(*self.guide_locators.LINK_HISTORICAL_ARCHIVE)
        self.action_move_to_element(archive_link)
        assert archive_link.is_enabled(), "The link is not clickable"

    def footer_click_allow(self):
        self.driver.find_element(*self.guide_locators.CLICK_ALLOW_IN_STICK_FOOTER).click()

    def verify_several_links_color(self, locator):
        links = self.driver.find_elements(*locator)
        for link in links:
            link_color_rgba = link.value_of_css_property("color")
            link_color_hex = Color.from_string(link_color_rgba).hex
            assert link_color_hex == BasePageMisc.EXPECTED_LINK_COLOR_HEX, f"The link color is {link_color_hex}, " \
                                                              f"while {BasePageMisc.EXPECTED_LINK_COLOR_HEX} is expected"

    def one_call_api_link_is_visible(self):
        one_call_api = self.driver.find_element(*GuideLocators.ONE_CALL_API_BY_CALL_LOCATOR)
        assert one_call_api.is_displayed(), "One call api link is not visible"


    def one_call_api_link_is_clickable(self):
        one_call_api = self.driver.find_element(*GuideLocators.ONE_CALL_API_BY_CALL_LOCATOR)
        assert one_call_api.is_enabled(), "One call api link is not clackable"

    def industry_standard_apis_link_redirection(self):
        element = self.driver.find_element(*GuideLocators.INDUSTRY_APIS_LOCATOR)
        self.driver.execute_script("arguments[0].click();", element)
        assert '/api' in self.driver.current_url, "The industry standard apis link leads to an incorrect page"

    def one_call_api_by_call_link_redirection(self):
        element = self.driver.find_element(*GuideLocators.ONE_CALL_API_BY_CALL_LOCATOR)
        self.driver.execute_script("arguments[0].click();", element)
        assert '/one-call-3' in self.driver.current_url, "The one call api by call link leads to an incorrect page"

    def subscribe_to_onecall_by_call_button_is_visible(self):
        subscribe_to_onecall_by_call_button = self.element_is_visible(GuideLocators.SUBSCRIBE_TO_ONE_CALL_BY_CALL_BUTTON)
        assert subscribe_to_onecall_by_call_button.is_displayed(), "The button 'subscribe to onecall by call' is not visible"


    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "Guide"
        displayed_title = self.driver.find_element(*self.guide_locators.DISPLAYED_TITLE).text
        assert displayed_title == expected_title
