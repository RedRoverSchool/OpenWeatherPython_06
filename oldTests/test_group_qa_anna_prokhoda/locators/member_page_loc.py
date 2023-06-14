from selenium.webdriver.common.by import By


class MemberPageLocators:
    email = (By.XPATH, '//input[@id="unauth_subscription_form_email"]')

    title = (By.XPATH, '//select[@id="unauth_subscription_form_title"]')
    title_options = (By.XPATH, '//select[@id="unauth_subscription_form_title"]//option')

    first_name = (By.XPATH, '//input[@id="unauth_subscription_form_first_name"]')
    last_name = (By.XPATH, '//input[@id="unauth_subscription_form_last_name"]')
    country = (By.XPATH, '//select[@id="unauth_subscription_form_country"]')
    address_1 = (By.XPATH, '//input[@id="unauth_subscription_form_address_line_1"]')
    address_2 = (By.XPATH, '//input[@id="unauth_subscription_form_address_line_2"]')
    city = (By.XPATH, '//input[@id="unauth_subscription_form_city"]')
    postal_code = (By.XPATH, '//input[@id="unauth_subscription_form_postal_code"]')
    state = (By.XPATH, '//input[@id="unauth_subscription_form_state"]')
    phone = (By.XPATH, '//input[@id="unauth_subscription_form_phone"]')

    continue_payment_button = (By.XPATH, '//input[@value="Continue to payment"]')

    legal_form_individual = (By.XPATH, '//span[@class="radio-inline"]//input[@value="individual"]')
    legal_form_organization = (By.XPATH, '//span[@class="radio-inline"]//input[@value="organisation"]')

    error_message = (By.XPATH, '//span[@class="help-block"]')

    payment = (By.XPATH, '//div[text()="Pay with card"]')