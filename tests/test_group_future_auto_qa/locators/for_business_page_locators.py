from selenium.webdriver.common.by import By


class ForBusinessPageLocators:
    FOR_BUSINESS = (By.CSS_SELECTOR, "div[id='desktop-menu'] a[class='marketplace']")
    PRODUCTS_IN_HEADER = (By.CSS_SELECTOR, "a[href='/products']")
    PRODUCTS_HEADINGS = (By.CSS_SELECTOR, "a big")
    ALLOW_ALL_COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
