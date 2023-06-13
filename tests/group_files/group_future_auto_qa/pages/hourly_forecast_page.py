from pages.base_page import BasePage
from tests.group_files.group_future_auto_qa.locators.hourly_forecast_page_locators import HourlyForecastPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HourlyForecastPage(BasePage):
    locators = HourlyForecastPageLocators()

    def check_redirects_of_anchor_links(self, wait, link_locator):
        self.driver.get("https://openweathermap.org/api/hourly-forecast")
        wait.until(EC.element_to_be_clickable(self.locators.ALLOW_ALL_COOKIES)).click()
        anchor_link = self.element_is_clickable(link_locator, 10)
        anchor_href = anchor_link.get_attribute("href")
        print(f"\nchecking link: {anchor_href}\nlink text: {anchor_link.text}")
        # title_locator = f"By.XPATH, "//section[@id='{anchor_href[47:]}']/*[1]""
        title_locator = f'//section[@id="{anchor_href[47:]}"]/*[1]'
        anchor_link.click()
        title = self.driver.find_element(By.XPATH, title_locator)
        # title = self.driver.find_element(title_locator)
        position_of_title = self.driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return {left: rect.left, top: rect.top};
        """, title)
        print(position_of_title['left'], " ", position_of_title['top'])
        assert position_of_title['left'] <= 280 and position_of_title['top'] <= 100, "Anchor link doesn't work"

    def check_page_title(self, page_title):
        self.driver.get("https://openweathermap.org/api/hourly-forecast")
        assert self.driver.title == page_title, "The title of the page is incorrect"

    def check_clickability_and_visibility_of_call_hourly_forecast_data_link(self, wait):
        self.driver.get("https://openweathermap.org/api/hourly-forecast")
        wait.until(EC.element_to_be_clickable(self.locators.ALLOW_ALL_COOKIES)).click()
        hourly_forecast_data_link = self.driver.find_element(*HourlyForecastPageLocators.CALL_HOURLY_FORECAST_DATA)
        wait.until(EC.element_to_be_clickable(hourly_forecast_data_link))
        assert hourly_forecast_data_link.is_displayed() and hourly_forecast_data_link.is_enabled(), \
            "Link is not displayed or not clickable"
