from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AskAQuestiontPage(BasePage):

    DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h4.headline')

    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "Ask a question"
        displayed_title = self.driver.find_element(*self.DISPLAYED_TITLE).text
        assert displayed_title == expected_title