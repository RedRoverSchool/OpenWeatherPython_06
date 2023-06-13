from selenium.webdriver.common.by import By


class SignInLocators:
    DIV_ALLERT_SUCCESSFULLY_LOGIN_GREEN = (By.CSS_SELECTOR, '.panel.panel-green')

class SignInURL:
    SIGN_IN_URL = 'https://home.openweathermap.org/users/sign_in'