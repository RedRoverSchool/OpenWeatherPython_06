from selenium.webdriver.common.by import By

class ApiPageLocators:
    LOGO = (By.CSS_SELECTOR, "#first-level-nav a")


class FooterLocators:
    footer_website_locator = (By.CLASS_NAME, "inner-footer-container")
    copyright_locator = (By.CSS_SELECTOR, "div.inner-footer-container div.horizontal-section.my-5 span:nth-child(3)")