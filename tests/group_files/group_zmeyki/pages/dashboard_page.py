from pages.base_page import BasePage
from tests.group_files.group_zmeyki.locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):
    locators = DashboardLocators()

    def verify_hourly_forecast_api_link_redirects_to_valid_page(self, wait):
        self.driver.get(self.locators.URL)
        dashboard_button = self.driver.find_element(*self.locators.dashboard_button_locator)
        self.driver.execute_script("arguments[0].click();", dashboard_button)
        hourly_forecast_api = self.driver.find_element(*self.locators.hourly_forecast_api_locator)
        self.driver.execute_script("arguments[0].click();", hourly_forecast_api)
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert '/api/hourly-forecast' in self.driver.current_url
