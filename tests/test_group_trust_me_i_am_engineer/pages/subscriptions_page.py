from selenium.webdriver.support import expected_conditions as EC
from pages import base_page
from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import SubscriptionsPageLocators
from selenium.webdriver import Keys


class SubscriptionsPage(BasePage):
    URL_SUBSCRIPTION = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/onecall_30/base'
    locators = SubscriptionsPageLocators()

    def verify_error_messages_for_empty_required_fields_in_organisation(self):
        expected_error_message = "can't be blank"
        expected_number_of_error_message = 6
        self.driver.get(self.URL_SUBSCRIPTION)
        radiobutton = self.driver.find_element(*self.locators.RADIOBUTTON_ORGANISATIONS)
        radiobutton.click()
        button = self.driver.find_element(*self.locators.BUTTON_CONTINUE_TO_PAYMENT)
        button.click()
        error_message = self.elements_are_visible(self.locators.ERROR_MESSAGE)
        checks = 0
        for i in error_message:
            assert i.is_displayed()
            checks += 1
        assert checks == expected_number_of_error_message, \
            "An error message 'can't be blank' does not appeared for fields marked as required."
