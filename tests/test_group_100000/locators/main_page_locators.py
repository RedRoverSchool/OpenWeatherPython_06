from selenium.webdriver.common.by import By


class FooterBlockLocators:
    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    HOW_TO_START_LINK = (By.CSS_SELECTOR, "div.section-content ul>li>a[href='/appid']")
