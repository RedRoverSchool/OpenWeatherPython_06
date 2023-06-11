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

    def check_submit_button_is_visible(self):
        submit_button = self.element_is_visible(self.locators.SUBMIT_BUTTON_DISPLAY)
        assert submit_button.is_displayed(), "Submit button is not visible"

    def check_link_for_password_recovery_is_visible(self):
        link_for_password_recovery = self.element_is_visible(self.locators.LINK_FOR_PASSWORD_RECOVERY_DISPLAY)
        assert link_for_password_recovery.is_displayed(), "Link for password recovery display is not visible"


class SigninPage(BasePage):
    locators = SignInLocator()

    def log_in(self):
        self.driver.find_element(*SignInLocator.EMAIL_INPUT).send_keys(cr.credentials["email"])
        self.driver.find_element(*SignInLocator.PASSWORD_INPUT).send_keys(cr.credentials["password"])
        self.driver.find_element(*SignInLocator.SUBMIT_BUTTON).click()

    def log_in_with_custom_values(self, email_text, password_text):
        self.driver.find_element(*SignInLocator.EMAIL_INPUT).send_keys(email_text)
        self.driver.find_element(*SignInLocator.PASSWORD_INPUT).send_keys(password_text)
        self.driver.find_element(*SignInLocator.SUBMIT_BUTTON).click()

    def confirm_error_message_is_visible(self):
        assert_massage = self.element_is_visible(self.locators.ERROR_LOGIN_MESSAGE_DIV)
        assert assert_massage, "Error: missing logging error message"
