from pages.base_page import BasePage
from tests.test_group_100000.locators.dashboard_page_locators import DashboardLocators as D


class DashboardPage(BasePage):
    def verify_display_of_how_to_start_section(self):
        self.click_header_link('dashboard')
        section = self.driver.find_element(*D.TITLE_HOW_TO_START)
        assert section.is_displayed(), "Section not found"