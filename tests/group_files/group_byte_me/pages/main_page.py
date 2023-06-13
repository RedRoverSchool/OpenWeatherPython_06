from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from tests.group_files.group_byte_me.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators()

    def click_header_weather_in_your_city_field(self):
        weather_in_your_city_field = self.driver.find_element(*self.locators.WEATHER_IN_YOUR_CITY_FLD)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(weather_in_your_city_field)
        self.driver.execute_script("arguments[0].click();", weather_in_your_city_field)
        return weather_in_your_city_field

    def fill_header_weather_in_your_city_field(self):
        input_weather_in_your_city_field = self.driver.find_element(*self.locators.WEATHER_IN_YOUR_CITY_FLD)
        input_weather_in_your_city_field.send_keys(*self.locators.REQUESTED_CITY)
        input_weather_in_your_city_field.submit()

    def displayed_text_is_the_same_as_the_entered_text(self, wait):
        displayed_text = wait.until(EC.visibility_of_element_located(self.locators.DISPLAYED_CITY)).text
        assert displayed_text == self.locators.REQUESTED_CITY

    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*self.locators.SEARCH_CITY_FIELD_locator)
        input_city.send_keys(city)

    def click_search_button(self, city):
        self.fill_city_search_field(city)
        self.driver.find_element(*self.locators.SEARCH_BUTTON_Locator).click()

    def check_search_city_result(self, wait, city):
        self.click_search_button(city)
        expected_city = city
        expected_error_message = f'No results for {city}'
        actual_error_message = self.element_is_displayed(self.locators.NO_RESULTS_NOTIFICATION, wait)
        if actual_error_message:
            actual_error_message_text = actual_error_message.text
            assert actual_error_message_text == expected_error_message, 'message = ogudaem'
        else:
            wait.until(EC.element_to_be_clickable(self.locators.SEARCH_OPTION_Locator)).click()
            wait.until(EC.text_to_be_present_in_element(self.locators.DISPLAYED_CITY_1_Locator, city))
            actual_city = self.driver.find_element(*self.locators.DISPLAYED_CITY_1_Locator).text
            assert expected_city in actual_city, 'gorod aktyal'
