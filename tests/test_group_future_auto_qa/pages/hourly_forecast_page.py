from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.hourly_forecast_page_locators import HourlyForecastPageLocators
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
        assert position_of_title['left'] <= 280 and position_of_title['top'] <= 100

    def check_page_title(self, page_title):
        self.driver.get("https://openweathermap.org/api/hourly-forecast")
        assert self.driver.title == page_title, "The title of the page is incorrect!"

