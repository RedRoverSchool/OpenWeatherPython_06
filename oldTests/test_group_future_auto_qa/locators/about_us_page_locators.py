from selenium.webdriver.common.by import By


class AboutUsLocators:
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, 'div.contact-us.blue-transparent-container.white-text a')
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'Allow all')]")