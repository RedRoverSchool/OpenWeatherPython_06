from selenium.webdriver.common.by import By


class ApiKeysLocator:
    API_KEY_NAME_URL = 'https://home.openweathermap.org/api_keys'
    API_KEY_EDIT_SELECTOR = By.CSS_SELECTOR, "i[class='fa fa-edit']"
    API_KEY_NAME_SELECTOR = By.XPATH, "//table/tbody/tr/td[2]"
    API_KEY_ENTER_SELECTOR = By.CSS_SELECTOR, "input[name='edit_key_form[name]']"
    SAVE_BUTTON_SELECTOR = By.CSS_SELECTOR, "button[class='button-round dark']"
    TAB_API_KEYS = By.CSS_SELECTOR, '#myTab [href="/api_keys"]'
    MODULE_API_KEY_CREATE = By.CSS_SELECTOR, '.col-md-4 h4'



