from tests.test_group_qa_anna_prokhoda.base.base_class import Base


class MemberPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #

    URL = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/weather/'
    pages = {"startup": "startup", "dev": "dev", "pro": "pro", "ent": "ent"}

    # Locators

    email = '//input[@id="unauth_subscription_form_email"]'

    title = '//select[@id="unauth_subscription_form_title"]'
    title_options = '//select[@id="unauth_subscription_form_title"]//option'

    first_name = '//input[@id="unauth_subscription_form_first_name"]'
    last_name = '//input[@id="unauth_subscription_form_last_name"]'
    country = '//select[@id="unauth_subscription_form_country"]'
    address_1 = '//input[@id="unauth_subscription_form_address_line_1"]'
    address_2 = '//input[@id="unauth_subscription_form_address_line_2"]'
    city = '//input[@id="unauth_subscription_form_city"]'
    postal_code = '//input[@id="unauth_subscription_form_postal_code"]'
    state = '//input[@id="unauth_subscription_form_state"]'
    phone = '//input[@id="unauth_subscription_form_phone"]'

    continue_payment_button = '//input[@value="Continue to payment"]'

    legal_form_individual = '//span[@class="radio-inline"]//input[1]'
    legal_form_organization = '//span[@class="radio-inline"]//input[2]'

    error_message = '//span[@class="help-block"]'

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
        self.find_elements_array(self.title_options)[option].click()
        print(f'Title option {self.find_elements_array(self.title_options)[option].text} clicked')

    """
    Method: verify the preselected country in the 'Country' field
    """

    def verify_country_text(self):
        result = self.find_element(self.country).text
        return result

    """
    Method: verify is the error message corresponds with the message from the requirements;
    Error message is the message, which appears when the form field is left bank
    Error message = "can't be blank"
    """

    def verify_error_message_text(self, number):
        error_text = self.find_element(self.error_message)[number].text
        print(f'Error message text: {error_text}')
        return error_text

    """
    Method: fill in only the required fields of the subscription form
    """

    def fill_in_required_fields(self):
        self.input_value(self.email, "test@test.com")
        self.input_value(self.first_name, "Test")
        self.input_value(self.last_name, "Test")
        self.input_value(self.address_1, "ul. Test, 1-11")
        self.input_value(self.city, "Test")
        self.input_value(self.postal_code, "11-111")
        self.input_value(self.phone, "111111111")

    """
    Method: check error message if every block (field), where it is necessary;
    As error message should appear only under required fields, we take this field block and check, 
    if there is am error message there
    """

    def check_error_messages(self):
        required_fields = ["email", "first_name", "last_name", "address_line_1", "city", "postal_code", "phone"]

        for i in range(len(required_fields)):
            error_message_in_field = f'//div[contains(@class, {required_fields[i]})]//span[@class="help-block"]'
            error_message = self.find_element(error_message_in_field)
            self.assert_text(error_message.text, "can't be blank")
            print(f'Error message {i} - OK')

    """
    Method: click 'Continue payment' button 
    """

    def click_continue_button(self):
        self.click_element(self.continue_payment_button)


















