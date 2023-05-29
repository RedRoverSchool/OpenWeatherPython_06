from selenium.webdriver.support import expected_conditions as EC
from pages import base_page
from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import PartnersPageLocators

class PartnersPage(BasePage):
    URL_PARTNERS = 'https://openweathermap.org/examples'
    locators = PartnersPageLocators()
    drupal_button = 'https://www.drupal.org/project/olowm'

    def verify_the_link_view_on_github_is_visible(self):
        self.driver.get(self.URL_PARTNERS)
        button = self.driver.find_element(*self.locators.BUTTON_VIEW_ON_GITHUB)
        self.go_to_element(button)
        assert button.is_displayed(), \
            "The 'View on Github' button is not displayed"

    def verify_redirection_drupal_button_leads_to_the_new_website(self):
        self.driver.get(self.URL_PARTNERS)
        button = self.driver.find_element(*self.locators.BUTTON_SEE_ON_THE_WEBSITE)
        self.driver.execute_script("arguments[0].click();", button)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.drupal_button, self.driver.current_url
