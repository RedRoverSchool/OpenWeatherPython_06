from pages.base_page import BasePage
from tests.test_group_100000.locators.dashboard_page_locators import DashboardLocators as D
from tests.test_group_100_000 import weather_symbol


class DashboardPage(BasePage):
    def verify_display_of_how_to_start_section(self):
        self.click_header_link('dashboard')
        section = self.driver.find_element(*D.TITLE_HOW_TO_START)
        assert section.is_displayed(), "Section not found"

class DashboardPage(BasePage):
    def test_TC_001_05_03_Verify_humidity_percentage_in_detailed_weather_data_for_current_location(self):
        humidity_symbol = self.driver.find_element(*weather_symbol)
        assert humidity_symbol.is_displayed()
