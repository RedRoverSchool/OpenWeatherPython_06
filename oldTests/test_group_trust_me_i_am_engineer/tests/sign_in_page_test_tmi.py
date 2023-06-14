from oldTests.test_group_trust_me_i_am_engineer.pages.sign_in_page import SignInPage
import pytest

def test_TC_014_01_04_verify_create_an_account_visibility(driver):
    page = SignInPage(driver)
    page.verify_link_create_an_account_is_displayed()
