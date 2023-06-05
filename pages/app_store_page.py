from pages.base_page import BasePage
from locators.locators import AppStorePageLocators


class AppStorePage(BasePage):
    locators = AppStorePageLocators

    def verify_element_on_page_url(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        expected_element = self.element_is_visible(self.locators.APP_TITLE)

        assert expected_element.text == "OpenWeather 4+"
