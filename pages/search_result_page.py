from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from locators.locators import SearchResultPageLocators
from locators.locators import MainPageLocators as MPL


class SearchResultPage(BasePage):
    locators = SearchResultPageLocators()

    def check_notification_display(self):
        expected_notification = "×\nNot found"
        wait(self.driver, timeout=5).until(EC.presence_of_element_located(self.locators.ALERT_NOTIFICATION))
        actual_notification = self.driver.find_element(*self.locators.ALERT_NOTIFICATION)
        actual_notification_text = actual_notification.text
        assert actual_notification_text == expected_notification

    def check_notification_is_closed(self):
        wait(self.driver, timeout=5).until(EC.presence_of_element_located(self.locators.ALERT_NOTIFICATION))
        self.driver.find_element(*self.locators.NOTIFICATION_BUTTON).click()
        assert len(self.driver.find_element(*self.locators.NOTIFICATION_PANE).get_attribute("innerHTML")) == 0

    def check_correspondence_of_entered_text(self, city):
        wait(self.driver, timeout=5).until(EC.presence_of_element_located(self.locators.STRING_ENTERED_CITY))
        search_result_city_name = self.driver.find_element(*self.locators.STRING_ENTERED_CITY)
        assert search_result_city_name.get_property("value") == city

    def check_chart_weather_is_displayed(self):
        chart = self.driver.find_element(*MPL.chart_weather)
        assert chart.is_displayed(), "Chart weather is not visible"

    def check_search_result_contains_city(self, city):
        cities = self.driver.find_elements(*MPL.result_locator)
        for city_name in cities:
            assert city in city_name.text
