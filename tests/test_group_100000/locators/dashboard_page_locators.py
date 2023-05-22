from selenium.webdriver.common.by import By


class DashboardLocators:
    BTN_DASHBOARD = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
    TITLE_HOW_TO_START = (By.XPATH, "//div/h2[contains(text(),'How to Start')]")

    TRY_THE_DASHBOARD2_BTN = (By.XPATH, "//div[6]//a[text()='Try the Dashboard']")
    PANEL_SIGN_IN_FORM = (By.CSS_SELECTOR, '.col-md-6 .panel-heading')

    WEATHER_SYMBOL = (By.CSS_SELECTOR, "ul  > li:nth-child(3) > span.symbol")
