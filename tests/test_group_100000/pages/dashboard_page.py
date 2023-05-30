from pages.base_page import BasePage
from tests.test_group_100000.locators.dashboard_page_locators import DashboardLocators as D


class DashboardPage(BasePage):
    def verify_display_of_how_to_start_section(self):
        self.click_header_link('dashboard')
        section = self.driver.find_element(*D.TITLE_HOW_TO_START)
        assert section.is_displayed(), "Section not found"

    def transition_to_another_page(self):
        self.click_header_link('dashboard')
        self.allow_all_cookies()
        self.driver.find_element(*D.TRY_THE_DASHBOARD2_BTN).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        alert_mms = self.driver.find_element(*D.PANEL_SIGN_IN_FORM)
        assert alert_mms.is_displayed(), 'WELCOME EVENTS'

    def verify_humidity_percentage_in_detailed_weather_data_for_current_location(self):
        humidity_symbol = self.driver.find_element(*D.WEATHER_SYMBOL)
        assert humidity_symbol.is_displayed()
