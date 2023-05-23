from selenium.webdriver.common.by import By
from tests.test_group_anna_prokhoda.base.base_class import Base
from tests.test_group_anna_prokhoda.locators.member_page_loc import MemberPageLocators as locator


class MemberPage(Base):

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
    Method: verify the preselected country in the 'Country' field
    """

    def verify_country_text(self, value):
        select_option = self.check_preselected_option(locator.country)
        self.assert_text(select_option, value)

    """
    Method: verify is the error message in concrete field corresponds with the message from the requirements;
    Error message is the message, which appears when the form field is left bank
    Error message = "can't be blank"
    """

    def verify_error_message_text(self, field, value):
        required_fields = {"email": "email",
                           "first_name": "first_name",
                           "last_name": "last_name",
                           "address_line_1": "address_line_1",
                           "city": "city",
                           "postal_code": "postal_code",
                           "phone": "phone"}
        error_message_in_field = (By.XPATH, f'//div[contains(@class, {required_fields.get(field)})]//span[@class="help-block"]')
        self.assert_text(self.find_element(error_message_in_field), value)

    """
    Method: fill in only the required fields of the subscription form
    """

    def fill_in_required_fields(self):
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
            error_message = self.find_element(error_message_in_field)
            self.assert_text(error_message, "can't be blank")
            print(f'Error message {i} - OK')

    """
    Method: click 'Continue payment' button 
    """

    def click_continue_button(self):
        self.click_element(locator.continue_payment_button)

    """
    Method: if 'Legal from' radio button is chosen by default
    """

    def check_radio_button_legal_form_selected(self):
        individual = self.check_element_selected(locator.legal_form_individual)
        organization = self.check_element_selected(locator.legal_form_organization)

        assert individual is True, \
            'Radio button "Individual" is not selected by default'
        assert organization is False, \
            'Radio button "Organization" is not selected by default'

    """
    Method: if 'Country' field is disabled
    """

    def check_country_field_disabled(self):
        result = self.check_property(locator.country, 'disabled')
        assert result is True, \
            'Country field is enabled'

    """
    Method: if the URL contain 'checkout.stripe.com' after transitioning to payment page
    """

    def check_payment_url(self):
        current_url = self.driver.current_url
        assert 'checkout.stripe.com' in current_url, \
            'The payment url is incorrect, no "checkout.stripe.com" inside'
