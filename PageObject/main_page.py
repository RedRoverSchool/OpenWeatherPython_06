from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage



class MainPage(BasePage):
    search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
    search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
    displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
    no_results_notification = (By.CSS_SELECTOR, '.widget-notification>span ')


    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*self.search_city_field)
        input_city.send_keys(city)


    def click_search_button(self, city):
        self.fill_city_search_field(city)
        self.driver.find_element(*self.search_button).click()

    def check_search_city_result(self, wait, city):
        self.click_search_button(city)
        expected_city = city
        expected_error_massage = f'No results for {city}'
        if self.element_is_displayed(*self.no_results_notification, wait):
            actual_error_message = wait.until(EC.visibility_of_element_located(self.no_results_notification))
            actual_error_message_text = actual_error_message.text
            assert actual_error_message_text == expected_error_massage
        else:
            wait.until(EC.element_to_be_clickable(self.search_dropdown_option)).click()
            wait.until(EC.text_to_be_present_in_element(self.displayed_city, city))
            actual_city = self.driver.find_element(*self.displayed_city).text
            assert expected_city in actual_city

