from pages.base_page import BasePage
from locators.locators import HowToStartLocators


class HowToStartPage(BasePage):
    how_to_start_locators = HowToStartLocators()

    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "How to start using professional collections"
        displayed_title = self.driver.find_element(*self.how_to_start_locators.DISPLAYED_TITLE).text
        assert displayed_title == expected_title