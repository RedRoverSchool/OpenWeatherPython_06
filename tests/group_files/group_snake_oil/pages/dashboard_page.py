from tests.group_files.group_snake_oil.locators.dashboard_locators import DashboardPageLocators
from pages.base_page import BasePage
import requests


class DashboardPage(BasePage):
    locators = DashboardPageLocators

    def click_the_text_link(self, locator):
        element = self.element_is_clickable(locator)
        href_link = element.get_attribute('href')
        new_tab = element.get_attribute('target') == '_blank'
        try:
            response = requests.get(href_link)
        except Exception:
            current_url = "NOT VALID",
            status_code = "no_status_code"
        else:
            element.click()
            if new_tab:
                self.driver.switch_to.window(self.driver.window_handles[1])
            current_url = self.driver.current_url
            status_code = response.status_code
        return current_url, status_code, href_link

    def verify_redirecting_to_expected_page(self, locator, expected_url):
        current_url, status_code, href_link = self.click_the_text_link(locator)
        assert current_url == expected_url and status_code == 200, \
            f"This URL '{href_link}' is redirecting to '{current_url}' URL. " \
            f"Expected URL is {expected_url}. Status code = {status_code}"

