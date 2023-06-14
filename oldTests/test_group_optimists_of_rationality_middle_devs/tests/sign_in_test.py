# Import for writing oldTests and debugging, not for Prod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# Imports required to work on Prod
from pages.base_page import BasePage
from oldTests.test_group_optimists_of_rationality_middle_devs.locators.sign_in_locators import SignInURL, SignInLocators
import pytest

from oldTests.test_group_optimists_of_rationality_middle_devs.pages.sign_in_page import SignInPage
from pages.sign_in_page import SigninPage

class TestSignIn:
    def test_TC_014_04_01_AT_014_04_01_01_Sign_in_Functionality_for_registered_User_Verify_authorization_with_valid_data_optimized(self, driver, open_and_load_sign_in_page, sign_in):
        """
        Triggering login through the created fixture
        (bypassing the main page, reducing test execution time)
        """
        page = SignInPage(driver)
        page.user_succesfuly_log_in(driver)

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
