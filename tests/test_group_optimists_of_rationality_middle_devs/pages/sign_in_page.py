# Import for writing tests and debugging, not for Prod
from selenium.webdriver.support.wait import WebDriverWait

# Imports required to work on Prod
from pages.base_page import BasePage
from tests.test_group_optimists_of_rationality_middle_devs.locators.sign_in_locators import *

class SignInPage(BasePage):
    URL = SignInURL.SIGNINURL
    print('===========')
    print(SignInURL.SIGNINURL, '#SignInURL()')
    print('===========')
    locators = SignInLocators()

    def open_sign_in_page(self, driver):
        driver.get(*self.URL)
        wait = WebDriverWait(driver, 3)

