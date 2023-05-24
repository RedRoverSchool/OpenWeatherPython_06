from selenium.webdriver.common.by import By

class FooterLocators:
    privacy_policy_link = (By.CSS_SELECTOR, 'div.section-content ul li:nth-child(2) a[href*="privacy-policy"]')
