from selenium.webdriver.common.by import By


class DashboardLocators:
    BTN_DASHBOARD = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
    TITLE_HOW_TO_START = (By.XPATH, "//div/h2[contains(text(),'How to Start')]")