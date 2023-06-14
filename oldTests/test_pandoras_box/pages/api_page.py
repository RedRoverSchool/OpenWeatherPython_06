from pages.base_page import BasePage
from locators.locators import ApiPageLocators
from selenium.webdriver.common.by import By


class APIPage(BasePage):
    button_weather_alerts_api_doc = (By.XPATH, "//*[@class='btn_block black round'][@href='/api/push-weather-alerts']")
    button_history_api_full_archive = (By.XPATH, "//*[@id='history']//*[@href='/api/history-api-full-archive']")
    DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
    actual_title_features = (By.XPATH, "//*[@id='about']/h2")
    GLOBAL_WEATHER_ALERTS_LINK = "https://openweathermap.org/api/push-weather-alerts"
    button_get_access = 'href="mailto:info@openweathermap.org"'

    def click_button_api_doc_history_full_archive(self):
        btn_history_api = self.driver.find_element(*self.button_history_api_full_archive)
        self.action_move_to_element(btn_history_api)
        self.driver.execute_script("arguments[0].click();", btn_history_api)

    def check_title_history_api_full_archive(self):
        actual_title_history_full = self.driver.find_element(*self.DISPLAYED_TITLE).text
        expected_title_history_full_archive = "History API Full archive"
        assert actual_title_history_full == expected_title_history_full_archive

    def click_button_api_doc_in_global_weather_alerts(self):
        btn_api = self.driver.find_element(*self.button_weather_alerts_api_doc)
        self.action_move_to_element(btn_api)
        self.driver.execute_script("arguments[0].click();", btn_api)

    def check_title_features_global_weather_alert(self):
        actual_title_features = self.driver.find_element(*self.actual_title_features).text
        expected_title_features = "Features of Global Weather Alerts"
        assert expected_title_features == actual_title_features

