from pages.sign_in_page import SignInPage
from test_data.urls import SignInUrls
from pages.sign_in_page import SigninPage #Someone did with a lowercase "i", this is not a double, if you remove this import, the oldTests below will break
from pages.main_page import MainPage
from test_data.urls import MainPageUrls


class TestSignInPage:

    def test_tc_014_03_01_checking_the_registration_question_display(self, driver):
        sign_in_question = SignInPage(driver, SignInUrls.url_sign_in_page)
        sign_in_question.open_page()
        element = sign_in_question.check_registration_question_is_visible()
        assert element is True, 'The element is not visible'

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

    def test_tc_014_01_05_verify_remember_me_record_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_remember_me_record_is_visible()

    def test_tc_014_01_06_verify_checkbox_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_checkbox_is_visible()

    def test_tc_014_01_07_verify_submit_button_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_submit_button_is_visible()

    def test_tc_014_01_08_verify_link_for_password_recovery_visibility(self, driver):
        page = SignInPage(driver, SignInUrls.url_sign_in_page)
        page.open_page()
        page.check_link_for_password_recovery_is_visible()

    def test_AT_014_06___Sign_in___Negative_testing_wrong_password___correct_login(self, driver, open_and_load_sign_in_page):
        """
        Negative testing of logging to the site
        Pair used:
        1. Valid E-mail
        2. NOT a valid password
        """
        page = SigninPage(driver)
        page.log_in_with_custom_values('2ta3ukw@fbpoint.net', ' ')
        page.confirm_error_message_is_visible()
