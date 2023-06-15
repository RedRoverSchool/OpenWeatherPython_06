from pages.base_page import BasePage
from locators.locators import ProfilePageLocators

class ProfilePage(BasePage):
    locators = ProfilePageLocators()

    def check_auth_notification(self):
        auth_notification_text = self.driver.find_element(*self.locators.AUTH_NOTIFICATION).text
        assert auth_notification_text == 'Signed in successfully.'
