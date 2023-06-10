from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.locators import ApiPageLocators
from locators.locators import FooterLocators as FL


class APIPage(BasePage):
    button_weather_alerts_api_doc = (By.XPATH, "//*[@id='current']//a[@href='/api/push-weather-alerts']")
    button_history_api_full_archive = (By.XPATH, "//*[@id='history']//*[@href='/api/history-api-full-archive']")
    GLOBAL_WEATHER_ALERTS_LINK = "https://openweathermap.org/api/push-weather-alerts"
    DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')

    def click_button_api_doc_history_full_archive(self):
        btn_history_api = self.driver.find_element(*self.button_history_api_full_archive)
        self.action_move_to_element(btn_history_api)
        self.driver.execute_script("arguments[0].click();", btn_history_api)


    def check_title_history_api_full_archive(self):
        actual_title_history_full = self.driver.find_element(*self.DISPLAYED_TITLE).text
        expected_title_history_full_archive = "History API Full archive"
        assert actual_title_history_full == expected_title_history_full_archive


    def verify_the_copyright_information_is_present_on_the_site_page(self):
        self.allow_all_cookies()
        expected_footer_text = "© 2012 — 2023 OpenWeather"
        footer = self.driver.find_element(*FL.FOOTER_COPYRIGHT)
        assert footer.is_displayed() and expected_footer_text in footer.text, \
            "The footer is not displayed or does not contain the expected text"

        
    def click_button_api_doc_history_full_archive(self):
        btn_history_api = self.driver.find_element(*self.button_history_api_full_archive)
        self.action_move_to_element(btn_history_api)
        self.driver.execute_script("arguments[0].click();", btn_history_api)


    def check_title_history_api_full_archive(self):
        actual_title_history_full = self.driver.find_element(*self.DISPLAYED_TITLE).text
        expected_title_history_full_archive = "History API Full archive"
        assert actual_title_history_full == expected_title_history_full_archive


class APIPage(BasePage):

    def verify_redirection_one_call_api_3_link(self):
        self.driver.get(ApiPageLocators.API_PAGE)
        self.driver.find_element(*ApiPageLocators.ONE_CALL_API_3).click()
        expected_link = ApiPageLocators.ONE_CALL_API_LINK
        assert self.driver.current_url == expected_link, "This link is not correct"
