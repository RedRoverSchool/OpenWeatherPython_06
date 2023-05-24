from selenium.webdriver.common.by import By


class SignInPageLocators:
    REGISTRATION_QUESTION = By.XPATH, "//p[contains(text(), 'Not registered?')]"
    REGISTRATION_FORM_DISPLAY = (By.CSS_SELECTOR, ".sign-form")
