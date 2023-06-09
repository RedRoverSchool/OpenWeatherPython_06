from locators.locators import PartnersLocators
from pages.base_page import BasePage
from test_data.urls import PartnersPageUrls
from test_data.all_links import Links
from test_data.partners_page_data import data


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

    def verify_the_link_view_on_github_is_visible(self):
        self.driver.get(Links.URL_PARTNERS)
        button = self.driver.find_element(*PartnersLocators.BUTTON_VIEW_ON_GITHUB)
        self.go_to_element(button)
        assert button.is_displayed(), \
            "The 'View on Github' button is not displayed"

    def verify_the_link_view_on_github_is_clickable(self):
        self.driver.get(Links.URL_PARTNERS)
        button = self.driver.find_element(*PartnersLocators.BUTTON_VIEW_ON_GITHUB)
        self.go_to_element(button)
        assert button.is_enabled(), \
            "The 'View on Github' button is not clickable"

    def verify_the_link_open_manual_is_visible(self):
        self.driver.get(Links.URL_PARTNERS)
        button = self.driver.find_element(*PartnersLocators.BUTTON_OPEN_MANUAL)
        self.go_to_element(button)
        assert button.is_displayed(), \
            "The 'Open manual' button is not displayed"

    def verify_the_link_open_manual_is_clickable(self):
        self.driver.get(Links.URL_PARTNERS)
        button = self.driver.find_element(*PartnersLocators.BUTTON_OPEN_MANUAL)
        self.go_to_element(button)
        assert button.is_enabled(), \
            "The 'Open manual' button is not clickable"

    def get_section_element(self, section):
        section_locator = (self.locators.HEADERS_ON_THE_PAGE[0], self.HEADERS_ON_THE_PAGE[1].format(section))
        section_element = self.element_is_present(section_locator)
        assert section_element.is_displayed(), f"Section '{section}' not found on the page"
        return section_element

    def verify_17_sections_are_visible(self):
        self.driver.get(Links.URL_PARTNERS)
        find_all_headers = self.driver.find_elements(*PartnersLocators.HEADERS_ON_THE_PAGE)
        headers_on_the_page = [i.text for i in find_all_headers]
        assert data["sections"] == headers_on_the_page
