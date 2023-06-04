from tests.test_group_bugs_in_each_step.pages.sign_in_page import SignInPage
from tests.test_group_bugs_in_each_step.test_data.urls import SignInUrls
from tests.test_group_bugs_in_each_step.pages.profile_page import ProfilePage
from test_data.credentials import credentials
import pytest


class TestRegistrationQuestion:

    def test_tc_014_03_01_checking_the_registration_question_display(self, driver):
        sign_in_question = SignInPage(driver, SignInUrls.url_sign_in_page)
        sign_in_question.open_page()
        element = sign_in_question.check_registration_question_is_visible()
        assert element is True, 'The element is not visible'

    def test_tc_014_04_02_verify_authorization_with_empty_fields(self, driver):
        sign_in_page = SignInPage(driver, SignInUrls.url_sign_in_page)
        sign_in_page.open_page()
        sign_in_page.check_authorization()
        sign_in_page.check_error_alert_text()

    def test_tc_014_01_01_verify_registration_form_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_registration_form_is_visible()

    def test_tc_014_01_02_verify_email_field_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_email_field_is_visible()

    def test_tc_014_01_03_verify_password_field_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_password_field_is_visible()

    def test_tc_014_04_01_verify_authorization_with_valid_data(self, driver):
        sign_in_page = SignInPage(driver, SignInUrls.url_sign_in_page)
        sign_in_page.open_page()
        sign_in_page.check_authorization(credentials['email'], credentials['password'])
        profile_page = ProfilePage(driver)
        profile_page.check_auth_notification()

    def test_tc_014_04_05_verify_authorization_with_valid_email_and_empty_password_field(self, driver):
        check_email_without_password = SignInPage(driver, SignInUrls.url_sign_in_page)
        check_email_without_password.open_page()
        check_email_without_password.check_authorization(credentials['email'])
        check_email_without_password.check_error_alert_text()

    def test_tc_014_04_06_verify_authorization_with_valid_password_and_empty_email_field(self, driver):
        check_password_without_email = SignInPage(driver, SignInUrls.url_sign_in_page)
        check_password_without_email.open_page()
        check_password_without_email.check_authorization(credentials['password'])
        check_password_without_email.check_error_alert_text()

    def test_tc_014_01_05_verify_remember_me_record_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_remember_me_record_is_visible()

    def test_tc_014_01_06_verify_checkbox_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_checkbox_is_visible()


class TestRegistrationLink:

    def test_tc_014_03_02_checking_the_link_to_the_registration_page_display(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_registration_link_is_visible()

    def test_tc_014_03_03_checking_clickability_of_registration_link(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_registration_link_is_clickable()

    def test_tc_014_03_04_checking_the_link_in_the_Sing_In_form_leads_to_the_registration_page(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_registration_link_functionality()

    def test_tc_014_01_07_verify_submit_button_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_submit_button_is_visible()
