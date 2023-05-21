from pages.base_page import *
from tests.test_group_ducktales.test_data import sign_in_page_data
from tests.test_group_ducktales.locators.sign_in_locators import SignInLocator



class SignInPage(BasePage):

    def log_in(self):
        self.driver.find_element(*SignInLocator.EMAIL_INPUT).send_keys(sign_in_page_data.USER_EMAIL)
        self.driver.find_element(*SignInLocator.PASSWORD_INPUT).send_keys(sign_in_page_data.USER_PASSWORD)
        self.driver.find_element(*SignInLocator.SUBMIT_BUTTON).click()
