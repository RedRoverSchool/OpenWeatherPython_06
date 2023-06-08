from locators.locators import PartnersLocators
from pages.base_page import BasePage
from test_data.urls import PartnersPageUrls


class PartnersPage(BasePage):
    locators = PartnersLocators()

    def verify_redirected_the_link_apache_camel_to_a_new_window(self, apache_camel):
        self.driver.get(PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        self.find_element_and_click(self.locators.APACHE_CAMEL_BUTTON)
        self.switch_to_new_window()
        apache_camel_link = self.driver.current_url
        assert apache_camel_link == apache_camel, "Incorrect link"

    def verify_visibility_and_clickability_the_link_apache_camel_to_a_new_window(self, apache_camel):
        self.driver.get(PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        assert self.element_is_visible(self.locators.APACHE_CAMEL_BUTTON) and self. \
            element_is_clickable(self.locators.APACHE_CAMEL_BUTTON), "Apache Camel is not visible or not clickable"

    def verify_visibility_and_clickability_git_button_python(self):
        self.driver.get(PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        link = self.element_is_clickable(self.locators.GIT_BUTTON_PYTHON)
        assert link.is_enabled(), "The 'View on Github' button is not clickable"

    def verify_redirection_git_button_python_to_the_new_webpage(self, git_button_python):
        self.driver.get(PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        self.find_element_and_click(self.locators.GIT_BUTTON_PYTHON)
        self.switch_to_new_window()
        git_button_python_link = self.driver.current_url
        assert git_button_python_link == git_button_python

    def verify_visibility_and_clickability_of_the_github_button_php(self, wait):
        self.driver.get(PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        assert self.element_is_displayed(self.locators.GIT_BUTTON_PHP, wait) and self. \
            element_is_clickable(self.locators.GIT_BUTTON_PHP), "GitHub PHP button is not visible or not clickable"

