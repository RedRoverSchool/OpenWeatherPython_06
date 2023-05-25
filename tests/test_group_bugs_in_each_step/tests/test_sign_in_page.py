from tests.test_group_bugs_in_each_step.pages.sign_in_page import SignInPage
from tests.test_group_bugs_in_each_step.test_data.urls import SignInUrls
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




