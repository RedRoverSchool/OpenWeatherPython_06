from pages.base_page import BasePage
from tests.test_group_bugs_in_each_step.locators.sign_in_page_locators import *
import requests
import time
import os


class SignInPage(BasePage):
    locators = SignInPageLocators()

    def sample_function(self):
        return self

    def check_registration_question_is_visible(self):
        registration_question = self.element_is_visible(self.locators.REGISTRATION_QUESTION)
        return registration_question.is_displayed()

    def check_authorization(self, email=None, password=None):
        if email:
            self.driver.find_element(*self.locators.EMAIL_INPUT).send_keys(email)
        if password:
            self.driver.find_element(*self.locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.locators.SUBMIT_BUTTON).click()

    def check_error_alert_text(self):
        error_alert_text = self.driver.find_element(*self.locators.ERROR_ALERT).text
        assert error_alert_text == 'Invalid Email or password.'

    def check_registration_form_is_visible(self):
        registration_form = self.element_is_visible(self.locators.REGISTRATION_FORM_DISPLAY)
        assert registration_form.is_displayed(), "Sign In To Your Account is not visible"

    def check_email_field_is_visible(self):
        email_field = self.element_is_visible(self.locators.EMAIL_FIELD_DISPLAY)
        assert email_field.is_displayed(), "Email field is not visible"

    def check_password_field_is_visible(self):
        password_field = self.element_is_visible(self.locators.PASSWORD_FIELD_DISPLAY)
        assert password_field.is_displayed(), "Password field is not visible"

    def check_remember_me_record_is_visible(self):
        remember_me_record = self.element_is_visible(self.locators.REMEMBER_ME_RECORD_DISPLAY)
        assert remember_me_record.is_displayed(), "Remember me record is not visible"

    def check_checkbox_is_visible(self):
        checkbox = self.element_is_visible(self.locators.CHECKBOX_DISPLAY)
        assert checkbox.is_displayed(), "Checkbox is not visible"

    def check_registration_link_is_visible(self):
        registration_link = self.element_is_visible(self.locators.CREATE_AN_ACCOUNT_LINK)
        assert registration_link.is_displayed(), "The Create an Account link is not visible"

    def check_registration_link_is_clickable(self):
        registration_link = self.driver.find_element(*self.locators.CREATE_AN_ACCOUNT_LINK)
        assert registration_link.is_enabled(), "The Create an Account link is not clickable"
