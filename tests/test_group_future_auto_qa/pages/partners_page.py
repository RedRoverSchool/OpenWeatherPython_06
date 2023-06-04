from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.partners_page_locators import PartnersLocators
from tests.test_group_future_auto_qa.test_data.urls import PARTNERS_AND_SOLUTIONS


class PartnersPage(BasePage):
    locators = PartnersLocators()
    git_button_python = 'https://github.com/csparpa/pyowm'

    def open(self):
        self.driver.get("https://openweathermap.org/examples#python")

    def verify_visibility_and_clickability_git_button_python(self):
        self.open()
        link = self.element_is_clickable(self.locators.GIT_BUTTON_PYTHON)
        assert link.is_enabled(), "The 'View on Github' button is not clickable"

    def verify_redirection_git_button_python_to_the_new_webpage(self):
        self.open()
        link = self.driver.find_element(*self.locators.GIT_BUTTON_PYTHON)
        self.driver.execute_script("arguments[0].click();", link)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.git_button_python, self.driver.current_url

    def verify_redirected_the_link_apache_camel_to_a_new_window(self, apache_camel):
        self.driver.get(PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        self.find_element_and_click(self.locators.APACHE_CAMEL_BUTTON)
        self.switch_to_new_window()
        apache_camel_link = self.driver.current_url
        assert apache_camel_link == apache_camel, "Incorrect link"

    def verify_visibility_and_clickability_the_link_apache_camel_to_a_new_window(self, apache_camel):
        self.driver.get(PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        assert self.element_is_visible(self.locators.APACHE_CAMEL_BUTTON) and self.\
            element_is_clickable(self.locators.APACHE_CAMEL_BUTTON), "Apache Camel is not visible or not clickable"
