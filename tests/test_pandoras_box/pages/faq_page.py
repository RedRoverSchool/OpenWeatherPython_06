from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FaqPage(BasePage):

    DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')

    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "Frequently Asked Questions"
        displayed_title = self.driver.find_element(*self.DISPLAYED_TITLE).text
        assert displayed_title == expected_title