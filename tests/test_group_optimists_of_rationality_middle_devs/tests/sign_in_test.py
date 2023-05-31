# Import for writing tests and debugging, not for Prod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Imports required to work on Prod
from pages.base_page import BasePage
from tests.test_group_optimists_of_rationality_middle_devs.locators.sign_in_locators import SignInURL, SignInLocators
import pytest

class TestSignIn:
    def test_TC_014_04_01_AT_014_04_01_01_Sign_in_Functionality_for_registered_User_Verify_authorization_with_valid_data_optimized(self, driver, open_and_load_sign_in_page, sign_in):
        """
        Triggering login through the created fixture
        (bypassing the main page, reducing test execution time)
        """
        assert driver.find_element(*SignInLocators.DIV_ALLERT_SUCCESSFULLY_LOGIN_GREEN)
