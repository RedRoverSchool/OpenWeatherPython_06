from selenium.webdriver.common.by import By


class CookiesSettingsPageLocators:
    COOKIES_SETTINGS_PAGE_LINK = "https://openweathermap.org/cookies-settings"
    COOKIES_THAT_ANALYSE_RADIOBUTTON = (By.CSS_SELECTOR, 'input#inlineCheckbox1:nth-child(1)')
    GOOGLE_ADVERTISING_RADIOBUTTON = (By.CSS_SELECTOR, 'input#inlineCheckbox2:nth-child(1)')
    SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, 'button#remove-stick-footer')
    SUCCESSFUL_SAVING_SETTINGS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-block')