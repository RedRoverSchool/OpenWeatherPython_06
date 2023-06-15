from pages.base_page import BasePage
from locators.locators import StudentInitiativeLocators

class StudentInitiativePage(BasePage):
    locators = StudentInitiativeLocators()


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