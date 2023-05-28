from pages.base_page import BasePage
from tests.test_group_ducktales.locators.main_locators import MainLocator
from tests.test_group_ducktales.test_data.main_page_data import *
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def get_day_by_weak(self):
        element = self.element_is_visible(MainLocator.FIRST_DAY_IN_8_DAY_FORECAST).text[:3]
        return element

    def get_day_by_computer(self):
        day_by_computer = datetime.now().weekday()
        today = WEEKDAYS[day_by_computer]
        return today

    def check_day(self):
        day_by_weak = self.get_day_by_weak()
        day_by_computer = self.get_day_by_computer()
        assert day_by_weak == f'{day_by_computer}', 'Module Search city widget contains the wrong day of the week '

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
        assert all(button.is_displayed() and button.is_enabled() for button in [metric_button, imperial_button]), \
            "Toggle buttons are not displayed or enabled"

    def check_app_store_brand_link_clickable(self):
        initial_page_number = len(self.driver.window_handles)
        self.go_to_module_download_openweather_app()
        app_store_brand_link = self.driver.find_element(*MainLocator.APP_STORE_BRAND_LINK)
        app_store_brand_link.click()
        actual_page_number = len(self.driver.window_handles)
        assert actual_page_number == initial_page_number + 1, \
            "The new web tab does not opened after click App Store brand-link's"

    def check_google_play_brand_link_clickable(self):
        initial_page_number = len(self.driver.window_handles)
        self.go_to_module_download_openweather_app()
        google_play_brand_link = self.driver.find_element(*MainLocator.GOOGLE_PLAY_BRAND_LINK)
        google_play_brand_link.click()
        actual_page_number = len(self.driver.window_handles)
        assert actual_page_number == initial_page_number + 1, \
            "The new web tab does not opened after click Google Play brand-link's"

    def check_google_play_brand_link_display(self):
        self.go_to_module_download_openweather_app()
        google_play_brand_link = self.driver.find_element(*MainLocator.GOOGLE_PLAY_BRAND_LINK)
        assert google_play_brand_link.is_displayed(), "Google Play brand-link is not displaying"

    def get_months(self):
        month = self.element_is_visible(MainLocator.FIRST_DAY_IN_8_DAY_FORECAST).text[5:-3]
        return month

    def get_months_by_computer(self):
        month_by_computer = datetime.now().month
        current_month = MONTHS[month_by_computer - 1]
        return current_month

    def check_months(self):
        page_month = self.get_months()
        page_month_by_computer = self.get_months_by_computer()
        assert page_month == f'{page_month_by_computer}'

    def find_search_city_input(self, key):
        self.driver.find_element(*MainLocator.SEARCH_CITY_INPUT).send_keys(key)

    def click_btn_search(self):
        element = self.driver.find_element(*MainLocator.BTN_SEARCH)
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()

    def check_dropdown_options(self):
        self.find_search_city_input(KEYS_FOR_SEARCH_CITY_INPUT)
        self.click_btn_search()
        dropdown_list = self.driver.find_elements(*MainLocator.DROPDOWN_LIST)
        for i in dropdown_list:
            assert 'California' in i.text, 'Not all search suggestions in the drop-down list contain "California"'

    def click_first_element_dropdown_menu(self):
        self.element_is_clickable(MainLocator.DROPDOWN_LIST, 10)
        self.driver.find_element(*MainLocator.DROPDOWN_LIST).click()
        self.element_is_present(MainLocator.SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT, 10)

    def get_city_text(self, wait):
        wait.until(EC.text_to_be_present_in_element(MainLocator.SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT, 'Atchison'))
        displayed_city = self.driver.find_element(*MainLocator.SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT).text
        return displayed_city

    def check_city_name_displayed_by_zip(self, wait):
        self.find_search_city_input(KEYS_FOR_SEARCH_CITY_INPUT_ZIP)
        self.click_btn_search()
        self.click_first_element_dropdown_menu()
        displayed_city = self.get_city_text(wait)
        assert displayed_city == EXPECTED_CITY



