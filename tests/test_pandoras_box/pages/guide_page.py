from selenium.webdriver.common.by import By
from tests.test_pandoras_box.pages.base_page import BasePage


class GuidePage(BasePage):

    DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')

    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "Guide"
        displayed_title = self.driver.find_element(*self.DISPLAYED_TITLE).text
        assert displayed_title == expected_title