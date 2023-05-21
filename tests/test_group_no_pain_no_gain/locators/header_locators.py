from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGO_LOCATOR = (By.CSS_SELECTOR, ".logo > a > img")
    PARTNERS_LINK = (By.CSS_SELECTOR, '#desktop-menu a[href="/examples"]')
