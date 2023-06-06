from pages.base_page import BasePage
from locators.locators import DashboardPageLocators as D


class DashboardPage(BasePage):
    def verify_display_of_how_to_start_section(self):
        self.click_header_link('dashboard')
        section = self.driver.find_element(*D.TITLE_HOW_TO_START)
        assert section.is_displayed(), "Section not found"

    def transition_to_another_page(self):
        self.click_header_link('dashboard')
        self.allow_all_cookies()
        self.find_element_and_click(D.TRY_THE_DASHBOARD2_BTN)
        self.switch_to_new_window()
        alert_mms = self.driver.find_element(*D.PANEL_SIGN_IN_FORM)
        assert alert_mms.is_displayed(), 'WELCOME EVENTS'

    def verify_humidity_percentage_in_detailed_weather_data_for_current_location(self):
        humidity_symbol = self.driver.find_element(*D.WEATHER_SYMBOL)
        assert humidity_symbol.is_displayed()
