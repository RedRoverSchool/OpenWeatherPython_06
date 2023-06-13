from pages.base_page import BasePage
from oldTests.test_group_trust_me_i_am_engineer.locators.page_locators import SignInPageLocators

class SignInPage(BasePage):
    locators = SignInPageLocators()
    SignIn_link = "https://home.openweathermap.org/users/sign_in"

    def verify_link_create_an_account_is_displayed(self):
        self.driver.get(self.SignIn_link)
        create_an_account = self.driver.find_element(*self.locators.CREATE_AN_ACCOUNT_LINK)
        self.go_to_element(create_an_account)
        assert create_an_account.is_displayed(), "Create An Account is not visible"
