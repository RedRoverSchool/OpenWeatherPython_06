from pages.base_page import BasePage
from tests.test_group_ducktales.locators.main_locators_d import MainLocator
from tests.test_group_ducktales.test_data.main_page_data_d import *
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
        assert page_month in f'{page_month_by_computer}'

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

    def click_first_element_dropdown_menu(self, wait):
        element_dropdown_menu = wait.until(EC.element_to_be_clickable(MainLocator.DROPDOWN_LIST))
        element_dropdown_menu.click()
        self.element_is_present(MainLocator.SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT, 10)

    def get_city_text(self, wait):
        wait.until(EC.text_to_be_present_in_element(MainLocator.SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT, 'Atchison'))
        displayed_city = self.driver.find_element(*MainLocator.SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT).text
        return displayed_city

    def check_city_name_displayed_by_zip(self, wait):
        self.find_search_city_input(KEYS_FOR_SEARCH_CITY_INPUT_ZIP)
        self.click_btn_search()
        self.click_first_element_dropdown_menu(wait)
        displayed_city = self.get_city_text(wait)
        assert displayed_city == EXPECTED_CITY

    def number_day_by_computer(self):
        return datetime.now().day

    def check_leap_year_for_february_days(self):
        year = datetime.now().year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            last_num = 29
        else:
            last_num = 28
        return last_num

    def find_number_of_days_in_a_month(self):
        month = self.get_months_by_computer()
        if month in MONTH_28:
            self.check_leap_year_for_february_days()
        elif month in MONTH_31:
            last_num = 31
        elif month in MONTH_30:
            last_num = 30
        return last_num

    def get_correct_list_num_days(self):
        correct_list = []
        first_num = self.number_day_by_computer()
        correct_list.append(first_num)
        number_of_days_in_a_month = self.find_number_of_days_in_a_month()
        for i in range(first_num + 1, first_num + 8):
            if i <= number_of_days_in_a_month:
                correct_list.append(i)
        len_correct_list = len(correct_list)
        if len_correct_list < 8:
            for i in range(1, 9 - len_correct_list):
                correct_list.append(i)
        return correct_list

    def get_num_days_by_page(self, driver):
        self.driver.find_element(*MainLocator.LIST_DAYS_IN_8_DAY_FORECAST).location_once_scrolled_into_view
        days_by_page = []
        days = driver.find_elements(*MainLocator.DAYS_IN_8_DAY_FORECAST_NUM)
        for day in days:
            days_by_page.append(day.text[-2:])
        days_by_page = list(map(int, days_by_page))
        return days_by_page

    def check_in_day_list_numbers_days(self, driver):
        expected_list = self.get_correct_list_num_days()
        actual_list = self.get_num_days_by_page(driver)
        assert actual_list == expected_list, 'Module Search city widget 8-day-forecast contains invalid day numbers'

    def verify_in_day_list_first_element_number_day(self):
        number_day = self.driver.find_element(*MainLocator.FIRST_DAY_IN_8_DAY_FORECAST).text[-2:]
        if number_day.startswith('0'):
            number_day = number_day[1:]
        number_day_by_computer = datetime.now().day
        assert number_day == f'{number_day_by_computer}'




