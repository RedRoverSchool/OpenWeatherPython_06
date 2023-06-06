from locators.locators import SignInLocator, SignInPageLocators
from pages.base_page import BasePage
from test_data import credentials as cr


class SignInPage(BasePage):
    locators = SignInPageLocators()

    def check_registration_question_is_visible(self):
        registration_question = self.element_is_visible(self.locators.REGISTRATION_QUESTION)
        return registration_question.is_displayed()

    def check_registration_link_is_visible(self):
        registration_link = self.element_is_visible(self.locators.CREATE_AN_ACCOUNT_LINK)
        assert registration_link.is_displayed(), "The Create an Account link is not visible"

    def check_registration_link_is_clickable(self):
        registration_link = self.driver.find_element(*self.locators.CREATE_AN_ACCOUNT_LINK)
        assert registration_link.is_enabled(), "The Create an Account link is not clickable"

    def check_registration_link_functionality(self):
        registration_link = self.driver.find_element(*self.locators.CREATE_AN_ACCOUNT_LINK)
        registration_link.click()
        assert '/sign_up' in self.driver.current_url, \
            "The Create an Account link leads to an incorrect page"


class SigninPage(BasePage):

    def log_in(self):
        self.driver.find_element(*SignInLocator.EMAIL_INPUT).send_keys(cr.credentials["email"])
        self.driver.find_element(*SignInLocator.PASSWORD_INPUT).send_keys(cr.credentials["password"])
        self.driver.find_element(*SignInLocator.SUBMIT_BUTTON).click()
