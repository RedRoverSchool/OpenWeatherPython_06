from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import OurInitiativesPageLocators
import requests
from tests.test_group_python_qa.links.links_all_pages import MAIN_PAGE


class OurInitiativesPage(BasePage):
    locator = OurInitiativesPageLocators

    def verify_main_logo(self):
        response = requests.get(MAIN_PAGE)
        assert response.status_code == 200

