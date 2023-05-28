from pages.base_page import BasePage
from tests.test_group_snake_oil.locators.footer_locators import FootersLocators


class Footer(BasePage):
    locators = FootersLocators

    def find_technologies_module(self):
        expected_footer_text = "Technologies"
        element = self.driver.find_element(*self.locators.FOOTER_TECHNOLOGIES)
        assert element.is_displayed() and expected_footer_text in element.text, \
            "The footer is not displayed or does not contain the expected text"

    def find_links_under_technologies_module(self, icon):
        element = self.driver.find_element(*icon)
        element_link = element.get_attribute('href')
        assert element.is_displayed() and element.is_enabled(), \
            f"Link {element_link} link is not visible/clickable on a page"
