from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.test_group_anna_prokhoda.locators.member_page_loc import MemberPageLocators as locator


class MemberPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #

    URL = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/weather/'
    pages = {"startup": "startup", "dev": "dev", "pro": "pro", "ent": "ent"}

    # Methods

    """
    Method: go to the link of the subscription option: startup, dev, pro, ent;
    Depends on what form you will fill in;
    All the fields in the forms are equal
    """

    def get_link(self, link):
        self.driver.get(f'{self.URL}{self.pages.get(link)}')

    """
    Method: choose the option in the 'Title' drop-down list
    As the field 'Title' is the drop-down list with options, 
    there is a possibility to choose one of the option from the list:
    [option] parameter is the number of the option from the list
    """

    def choose_title_option(self, option):
        self.select_option_from_list(locator.title, option)

    """
    Method: fill in only the required fields of the subscription form
    """

    def fill_in_fields(self, title=None, address_2=None, state=None):
        if title:
            self.select_option_from_list(locator.title, title)
        if address_2:
            self.input_value(locator.address_2, "ul. Test, 2-22")
        if state:
            self.input_value(locator.state, "Test")
        self.input_value(locator.email, "test@test.com")
        self.input_value(locator.first_name, "Test")
        self.input_value(locator.last_name, "Test")
        self.input_value(locator.address_1, "ul. Test, 1-11")
        self.input_value(locator.city, "Test")
        self.input_value(locator.postal_code, "11-111")
        self.input_value(locator.phone, "111111111")

    """
    Method: check error message if every block (field), where it is necessary;
    As error message should appear only under required fields, we take this field block and check, 
    if there is am error message there
    """

    def check_error_messages(self):
        required_fields = ["email", "first_name", "last_name", "address_line_1", "city", "postal_code", "phone"]

        for i in range(len(required_fields)):
            error_message_in_field = (By.XPATH, f'//div[contains(@class, {required_fields[i]})]//span[@class="help-block"]')
            error_message = self.element_is_present(error_message_in_field)
            self.assert_text(error_message, "can't be blank")
            print(f'Error message {i} - OK')

    """
    Method: click 'Continue payment' button 
    """

    def click_continue_button(self):
        self.action_move_to_element(self.element_is_clickable(locator.continue_payment_button))
        print('Moved to button')
        self.click_element(locator.continue_payment_button)

    """
    Method: if the URL contain 'checkout.stripe.com' after transitioning to payment page
    """

    def check_payment_url(self):
        current_url = self.driver.current_url
        assert 'checkout.stripe.com' in current_url, \
            'The payment url is incorrect, no "checkout.stripe.com" inside'
