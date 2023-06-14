from pages.base_page import BasePage
from locators.locators import StudentInitiativeLocators
from locators.locators import SignInPageLocators

class StudentInitiativePage(BasePage):
    locators = StudentInitiativeLocators()
    signin_locator = SignInPageLocators()


    def verify_website_link_redirects_to_main_page(self, wait):
        self.driver.get('https://openweathermap.org/our-initiatives/student-initiative')
        website_link = self.driver.find_element(*self.locators.WEBSITE_LINK_LOCATOR)
        self.driver.execute_script("arguments[0].click();", website_link)
        assert self.driver.current_url == 'https://openweathermap.org/'

    def verify_correct_redirection_to_popup_window(self, wait):
        self.driver.get('https://openweathermap.org/our-initiatives/student-initiative')
        ask_us_popup = self.driver.find_element(*self.locators.ASK_US_POPUP_LOCATOR)
        self.driver.execute_script("arguments[0].click();", ask_us_popup)
        assert ask_us_popup.is_displayed() and ask_us_popup.is_enabled()

    def check_open_autorization(self):
        get_access = self.driver.find_element(*self.locators.BUTTON_GET_ACCESS)
        self.action_move_to_element(get_access)
        self.driver.execute_script("arguments[0].click();", get_access)
        expected_title = 'Sign In To Your Account'
        displayed_title = self.driver.find_element(*self.signin_locator.DISPLAYED_AUTHORISATION_HEADER).text
        assert displayed_title == expected_title
