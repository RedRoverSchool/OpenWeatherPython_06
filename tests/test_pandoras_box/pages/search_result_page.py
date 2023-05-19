from selenium.webdriver.common.by import By
from tests.test_pandoras_box.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class SearchResultPage(BasePage):
    ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#forecast_list_ul .alert.alert-warning")
    STRING_ENTERED_CITY = (By.CSS_SELECTOR, "#search_str")

    def check_notification_display(self):
        expected_notification = "×\nNot found"
        wait(self.driver, timeout=5).until(EC.presence_of_element_located(self.ALERT_NOTIFICATION))
        actual_notification = self.driver.find_element(*self.ALERT_NOTIFICATION)
        actual_notification_text = actual_notification.text
        assert actual_notification_text == expected_notification
