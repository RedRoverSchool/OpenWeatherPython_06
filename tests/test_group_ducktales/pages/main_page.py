from pages.base_page import BasePage
from tests.test_group_ducktales.locators.main_locators import MainLocator
from tests.test_group_ducktales.test_data.main_page_data import *
from datetime import datetime


class MainPage(BasePage):

    def get_day_by_weak(self):
        element = self.element_is_visible(MainLocator.FIRST_DAY_IN_8_DAY_FORECAST).text[:3]
        return element

    def day_by_computer(self):
        day_by_computer = datetime.now().weekday()
        today = WEEKDAYS[day_by_computer]
        return today

    def go_to_module_download_openweather_app(self):
        module_download_openweather_app = self.driver.find_element(*MainLocator.MODULE_DOWNLOAD_OPENWEATHER_APP)
        self.go_to_element(module_download_openweather_app)
        return module_download_openweather_app

    def check_module_title_download_openweather_app(self):
        module_download_openweather_app = self.go_to_module_download_openweather_app()
        assert module_download_openweather_app.is_displayed(), "Module title Download openweather app is not display"

    def check_app_store_brand_link_display(self):
        self.go_to_module_download_openweather_app()
        app_store_brand_link = self.driver.find_element(*MainLocator.APP_STORE_BRAND_LINK)
        assert app_store_brand_link.is_displayed(), "The brand-link for Download on the App Store is not displaying"

    def check_buttons_displayed_and_enabled(self):
        imperial_button = self.driver.find_element(*MainLocator.TO_IMPERIAL_BTN)
        metric_button = self.driver.find_element(*MainLocator.TO_METRIC_BTN)
        assert all(button.is_displayed() and button.is_enabled() for button in [metric_button, imperial_button]),\
            "Toggle buttons are not displayed or enabled"
