from locators.locators import SignInLocator
from pages.base_page import BasePage
from test_data import credentials as cr


class SigninPage(BasePage):

    def log_in(self):
        self.driver.find_element(*SignInLocator.EMAIL_INPUT).send_keys(cr.credentials["email"])
        self.driver.find_element(*SignInLocator.PASSWORD_INPUT).send_keys(cr.credentials["password"])
        self.driver.find_element(*SignInLocator.SUBMIT_BUTTON).click()
