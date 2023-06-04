from pages.sign_in_page import SignInPage
from test_data.urls import SignInUrls


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
