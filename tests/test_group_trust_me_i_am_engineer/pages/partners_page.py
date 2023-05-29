from selenium.webdriver.support import expected_conditions as EC
from pages import base_page
from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import PartnersPageLocators

class PartnersPage(BasePage):
    URL_PARTNERS = 'https://openweathermap.org/examples'
    locators = PartnersPageLocators()

    def verify_the_link_view_on_github_is_visible(self):
        self.driver.get(self.URL_PARTNERS)
        button = self.driver.find_element(*self.locators.BUTTON_VIEW_ON_GITHUB)
        self.go_to_element(button)
        assert button.is_displayed(), \
            "The 'View on Github' button is not displayed"
