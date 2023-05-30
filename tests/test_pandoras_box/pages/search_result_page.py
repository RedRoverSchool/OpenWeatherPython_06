from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from pages.main_page import MainPage


class SearchResultPage(BasePage):
    ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#forecast_list_ul .alert.alert-warning")
    STRING_ENTERED_CITY = (By.CSS_SELECTOR, "#search_str")
    NOTIFICATION_PANE = (By.ID, 'forecast_list_ul')
    NOTIFICATION_BUTTON = (By.CSS_SELECTOR, '.alert.alert-warning a.close')
    result_locator = (By.XPATH, '//a[contains(@href, "city")]')
    KEY_SEARCH_CITY = 'Saint Petersburg'
    METRIC_SWITCH = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")

    def check_notification_display(self):
        expected_notification = "×\nNot found"
        wait(self.driver, timeout=5).until(EC.presence_of_element_located(self.ALERT_NOTIFICATION))
        actual_notification = self.driver.find_element(*self.ALERT_NOTIFICATION)
        actual_notification_text = actual_notification.text
        assert actual_notification_text == expected_notification

    def check_notification_is_closed(self):
        wait(self.driver, timeout=5).until(EC.presence_of_element_located(self.ALERT_NOTIFICATION))
        self.driver.find_element(*self.NOTIFICATION_BUTTON).click()
        assert len(self.driver.find_element(*self.NOTIFICATION_PANE).get_attribute("innerHTML")) == 0

    def check_correspondence_of_entered_text(self, city):
        wait(self.driver, timeout=5).until(EC.presence_of_element_located(self.STRING_ENTERED_CITY))
        search_result_city_name = self.driver.find_element(*self.STRING_ENTERED_CITY)
        assert search_result_city_name.get_property("value") == city


    def check_search_result_contains_city(self, city):
        cities = self.driver.find_elements(*self.result_locator)
        for city_name in cities:
            assert city in city_name.text

    def dropdown_contain_city_temperature(self):
        metric_button = wait(self.driver, timeout=5).until(EC.element_to_be_clickable(self.METRIC_SWITCH))
        assert metric_button.is_displayed() and metric_button.is_enabled()
        search_city_input = self.driver.find_element(*MainPage.search_city_field)
        search_city_input.click()
        search_city_input.send_keys(*self.KEY_SEARCH_CITY)
        self.driver.find_element(*MainPage.search_button).click()
        dropdown_list = self.driver.find_elements(*MainPage.search_dropdown)
        for city in dropdown_list:
            assert '°C' in city.text
