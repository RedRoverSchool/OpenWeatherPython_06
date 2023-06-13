from selenium.webdriver.common.by import By


class CookiesSettingsLocators:
    RADIO_BUTTON_1 = (By.XPATH, '(//div/input)[1]')
    RADIO_BUTTON_2 = (By.XPATH, '(//div/input)[2]')
    RADIO_BUTTON_3 = (By.XPATH, '(//div/input)[3]')
    RADIO_BUTTON_4 = (By.XPATH, '(//div/input)[4]')
    LEARN_MORE_COOKIES = (By.CSS_SELECTOR, "a[href='/cookies-details']")
    SAVE_CHANGES_BUTTON = (By.XPATH, "//*[contains(text(), 'Save')]")
