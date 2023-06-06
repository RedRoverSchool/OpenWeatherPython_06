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

    def verify_17_sections_are_visible(self):
        self.driver.get(Links.URL_PARTNERS)
        find_all_headers = self.driver.find_elements(*PartnersLocators.HEADERS_ON_THE_PAGE)
        headers_on_the_page = [i.text for i in find_all_headers]
        assert data["sections"] == headers_on_the_page

    def link_see_library_visibility(self, wait):
        self.element_is_displayed(PartnersLocators.LINK_SEE_LIBRARY, wait)

    def link_see_library_is_clickable(self, wait):
        see_library_link = self.element_is_clickable(PartnersLocators.LINK_SEE_LIBRARY)
        assert see_library_link.is_enabled(), "The link is not clickable"

    def redirecting_to_more_details_with_source_code_page(self, wait):
        more_details_link = self.driver.find_element(*PartnersLocators.MORE_DETAILS_LOCATOR)
        self.driver.execute_script("arguments[0].click();", more_details_link)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        weather_based = self.driver.find_element(*PartnersLocators.WEATHER_BASED_COMPAIGN_MANAGEMENT)
        assert weather_based.is_displayed(), 'Weather-based Campaign Management header is not on this page'

    def verify_wordpress_awesome_weather_widget_leads_to_the_new_website(self):
        self.driver.get(PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        self.find_element_and_click(self.locators.BUTTON_SEE_ON_THE_WEBSITE)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert 'https://www.drupal.org/project/olowm' in self.driver.current_url, \
        "See on the website link leads to an incorrect page"

    def verify_the_link_view_solutions_leads_to_the_new_website(self):
        self.driver.get(PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        self.find_element_and_click(self.locators.BUTTON_VIEW_SOLUTIONS)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert PartnersPageUrls.REPOSITORIES_OPENWEATHER, self.driver.current_url

    def verify_redirection_github_php_button_to_the_new_webpage(self):
        self.driver.get(PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        self.allow_all_cookies()
        self.find_element_and_click(self.locators.GIT_BUTTON_PHP)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert PartnersPageUrls.GIT_PHP_URL, self.driver.current_url

    def verify_17_anchor_links_redirection(self):
        address_bar = "https://openweathermap.org/examples#"
        anchor_links_locator = PartnersLocators.ANCHORS_LOCATOR
        anchor_links = self.driver.find_elements(*anchor_links_locator)
        for anchor_link in anchor_links:
            self.scroll_to_the_element(anchor_links_locator)
            anchor_link.click()
            href = anchor_link.get_attribute("href")
            assert address_bar in self.driver.current_url and href == self.driver.current_url, \
                f"Redirection of the anchor link {href} is not successful"

    def verify_visibility_and_clickability_youtube_button_pyowm(self):
        self.driver.get(PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        link = self.element_is_clickable(self.locators.YOUTUBE_BUTTON_PYOWM)
        assert link, "The 'View on Youtube' button is not clickable"
