from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators

class MainPage(BasePage):
    locators = MainPageLocators()

    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*self.locators.SEARCH_CITY_FIELD)
        input_city.send_keys(city)

    def search_city(self, city):
        self.fill_city_search_field(city)
        self.driver.find_element(*self.locators.SEARCH_BUTTON).click()

    def check_seach_city_result(self, wait, city):
        self.click_search_button(city)
        expected_city = city
        expected_error_message = f'No results for {city}'
        if self.element_is_displayed(self.locators.NO_RESULTS_NOTIFICATION, wait):
            actual_error_message = wait.until(EC.visibility_of_element_located(self.locators.NO_RESULTS_NOTIFICATION))
            actual_error_message_text = actual_error_message.text
            assert actual_error_message_text == expected_error_message
        else:
            wait.until(EC.element_to_be_clickable(self.locators.SEARCH_DROPDOWN_OPTION)).click()
            wait.until(EC.text_to_be_present_in_element(self.locators.DISPLAYED_CITY, city))
            actual_city = self.driver.find_element(*self.locators.DISPLAYED_CITY).text
            assert expected_city in actual_city

    def go_to_about_us_page_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.allow_all_cookies()
        main_page.element_is_clickable(self.locators.ABOUT_US_BUTTON).click()

    def choose_1st_option(self, wait):
        wait.until(EC.element_to_be_clickable(self.locators.SEARCH_DROPDOWN_OPTION)).click()

    def switch_to_c_temp(self):
        self.driver.find_element(*self.locators.C_TEMP_LOCATOR).click()

    def check_8_lines_are_displayed(self):
        lines = self.driver.find_elements(*self.locators.LINE_IN_8_DAYS_FORECAST_LOCATOR)
        for line in lines:
            assert line.is_displayed()

