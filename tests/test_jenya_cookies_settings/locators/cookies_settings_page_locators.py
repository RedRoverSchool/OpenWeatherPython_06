from selenium.webdriver.common.by import By

class CookiesSettingsPageLocators:



    TITLE_COOKIES_SETTINGS = (By.XPATH, "//h1[contains(text(),'Cookies settings')]")
    COOKIES_ANALYSE_CHECKBOX_ON = (By.XPATH, "//input[contains(@id,'inlineCheckbox1')][1]")
    COOKIES_ANALYSE_CHECKBOX_OFF = (By.XPATH, "//input[contains(@id,'inlineCheckbox1')][2]")
    COOKIES_ANALYSE_NAME_ON = (By.XPATH, "//input[@id='inlineCheckbox1']/preceding-sibling::label[contains(text(), 'On')]")
    COOKIES_ANALYSE_NAME_OFF = (By.XPATH, "//input[contains(@id,'inlineCheckbox1')][2]/following-sibling::*")

    COOKIES_GOOGLE_ADVERTISING_CHECKBOX_ON = (By.XPATH, "//input[contains(@id,'inlineCheckbox2')][1]")
    COOKIES_GOOGLE_ADVERTISING_CHECKBOX_OFF = (By.XPATH, "//input[contains(@id,'inlineCheckbox2')][2]")
    COOKIES_GOOGLE_ADVERTISING_NAME_ON = (By.XPATH, "//input[@id='inlineCheckbox2']/preceding-sibling::label[contains(text(), 'On')]")
    COOKIES_GOOGLE_ADVERTISING_NAME_OFF = (By.XPATH, "//input[contains(@id,'inlineCheckbox2')][2]/following-sibling::*")
    FOOTER = (By.XPATH, "//button[contains(text(),'Allow all')]")

    SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, "button#remove-stick-footer")

    COOKIES_SAVED_MESSAGE = (By.XPATH, "//b[contains(text(), 'Your cookie settings were saved')]")