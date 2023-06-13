from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class StudentInitiative(BasePage):

    STUDENT_INITIATIVE_URL = 'https://openweathermap.org/our-initiatives/student-initiative'
    BUTTON_GET_ACCESS = (By.XPATH, '//a[text()="Get access"]')
    DISPLAYED_AUTHORISATION_WINDOW = (By.XPATH, '//h3[text()="Sign In To Your Account"]')

    def check_open_autorization(self):
        get_access = self.driver.find_element(*self.BUTTON_GET_ACCESS)
        self.action_move_to_element(get_access)
        self.driver.execute_script("arguments[0].click();", get_access)
        expected_title = 'Sign In To Your Account'
        displayed_title = self.driver.find_element(*self.DISPLAYED_AUTHORISATION_WINDOW).text
        assert displayed_title == expected_title
