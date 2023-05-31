from selenium.webdriver.common.by import By


class SignInPageLocators:
    REGISTRATION_QUESTION = By.XPATH, "//p[contains(text(), 'Not registered?')]"
    EMAIL_INPUT = (By.XPATH, "//input[@class='string email optional form-control']")
    PASSWORD_INPUT = (By.XPATH, "//input[@class='form-control']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@class='simple_form new_user']/input[3]")
    ERROR_ALERT = (By.XPATH, "//div[@class='panel-body']")
    REGISTRATION_FORM_DISPLAY = (By.CSS_SELECTOR, ".sign-form")
    EMAIL_FIELD_DISPLAY = (By.CSS_SELECTOR, ".new_user > :nth-child(3)")
    PASSWORD_FIELD_DISPLAY = (By.CSS_SELECTOR, "#user_password")
    REMEMBER_ME_RECORD_DISPLAY = (By.CSS_SELECTOR, "label.boolean")