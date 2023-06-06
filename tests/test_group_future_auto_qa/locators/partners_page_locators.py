from selenium.webdriver.common.by import By


class PartnersLocators:
    GIT_BUTTON_PYTHON = (By.CSS_SELECTOR, 'a[href*="github.com/csparpa/pyowm"]')
    APACHE_CAMEL_BUTTON = (By.CSS_SELECTOR, 'a[href*="camel.apache"]')
    GIT_BUTTON_PHP = (By.CSS_SELECTOR, 'a[href*="php"]')
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    YOUTUBE_BUTTON_PYOWM = (By.CSS_SELECTOR, '#python > a[href*="youtube"]')

