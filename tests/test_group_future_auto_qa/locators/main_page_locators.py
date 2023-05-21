from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_SEARCH_FIELD = (By.NAME, "q")
    HEADER_SEARCH_PLACEHOLDER = (By.CSS_SELECTOR, 'input[name="q"]::placeholder')
    WIDGETS = (By.XPATH, "//a[contains(text(), 'Widgets')]")
    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")


