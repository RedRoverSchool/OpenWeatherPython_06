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
