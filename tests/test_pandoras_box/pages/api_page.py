from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ApiPage(BasePage):
    button_weather_alerts_api_doc = (By.XPATH, "//*[@id='current']//a[@href='/api/push-weather-alerts']")
    actual_title_features = (By.XPATH, "// *[ @ id = 'about'] / h2")

    def click_button_api_doc_in_global_weather_alerts(self):
        btn_api = self.driver.find_element(*self.button_weather_alerts_api_doc)
        self.action_move_to_element(btn_api)
        self.driver.execute_script("arguments[0].click();", btn_api)


    def check_title_features_global_weather_alert(self):
        actual_title_features = self.driver.find_element(*self.actual_title_features).text
        expected_title_features = "Features of Global Weather Alerts"
        assert expected_title_features == actual_title_features
