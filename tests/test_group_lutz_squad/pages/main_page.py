from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from tests.test_group_lutz_squad.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*MainPageLocators.search_city_field_locator)
        input_city.send_keys(city)

    def click_search_button(self, city):
        self.fill_city_search_field(city)
        self.driver.find_element(*MainPageLocators.search_button_locator).click()

    def check_search_city_result(self, wait, city):
        self.click_search_button(city)
        expected_city = city
        expected_error_message = f'No results for {city}'
        if self.element_is_displayed(MainPageLocators.no_results_notification, wait):
            actual_error_message = wait.until(EC.visibility_of_element_located(MainPageLocators.no_results_notification))
            actual_error_message_text = actual_error_message.text
            assert actual_error_message_text == expected_error_message
        else:
            wait.until(EC.element_to_be_clickable(MainPageLocators.search_option_locator)).click()
            wait.until(EC.text_to_be_present_in_element(MainPageLocators.displayed_city_locator, city))
            actual_city = self.driver.find_element(*MainPageLocators.displayed_city_locator).text
            assert expected_city in actual_city

    def about_us_link_leads_to_correct_page(self):
        about_us_link = self.driver.find_element(*MainPageLocators.ABOUT_US_LOCATOR)
        self.go_to_element(about_us_link)
        about_us_link.click()
        assert self.driver.current_url == 'https://openweathermap.org/about-us'
