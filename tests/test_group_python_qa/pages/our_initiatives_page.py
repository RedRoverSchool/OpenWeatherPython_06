from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import OurInitiativesPageLocators
import requests


class OurInitiativesPage(BasePage):
    URL_OUR_INITIATIVES_PAGE = 'https://openweathermap.org/our-initiatives'
    URL_MAIN_PAGE = 'https://openweathermap.org/'
    locator = OurInitiativesPageLocators

    def verify_main_logo(self):
        self.driver.get(self.URL_OUR_INITIATIVES_PAGE)
        m_logo = self.driver.find_element(*self.locator.MAIN_LOGO)
        m_logo.click()
        response = requests.get(self.URL_MAIN_PAGE)
        assert response.status_code == 200

