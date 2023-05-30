from selenium.webdriver.common.by import By


class ApiKeysLocator:
    API_KEY_NAME_URL = 'https://home.openweathermap.org/api_keys'
    API_KEY_EDIT_SELECTOR = By.CSS_SELECTOR, "i[class='fa fa-edit']"
    API_KEY_NAME_SELECTOR = By.XPATH, "//table/tbody/tr/td[2]"
    API_KEY_ENTER_SELECTOR = By.CSS_SELECTOR, "input[name='edit_key_form[name]']"
    SAVE_BUTTON_SELECTOR = By.CSS_SELECTOR, "button[class='button-round dark']"
    TAB_API_KEYS = By.CSS_SELECTOR, '#myTab [href="/api_keys"]'
    MODULE_API_KEY_CREATE = By.CSS_SELECTOR, '.col-md-4 h4'
    EDIT_API_KEY_ICON = By.CSS_SELECTOR, '.edit_key_btn .fa-edit'
    API_KEY_FIELD = (By.CSS_SELECTOR, '#new_edit_key_form .owm_input')
    SAVE_NEW_API_NAME_BUTTON = By.CSS_SELECTOR, '.pop-up-footer .button-round.dark'
    API_KEY_NAME_FIRST_ROW = By.XPATH, "//div[@class='col-md-8']//tr[1]//td[2]"
    NEW_API_KEY_NAME = By.CSS_SELECTOR, ".new_api_key_form .owm_input"
    GENERATE_BUTTON = By.CSS_SELECTOR, '.new_api_key_form .button-round.dark'
    TABLE_API_KEYS = By.CSS_SELECTOR, "tbody tr"
    NOTICE_MESSAGE = By.XPATH, "//div[@class='panel-body']"



