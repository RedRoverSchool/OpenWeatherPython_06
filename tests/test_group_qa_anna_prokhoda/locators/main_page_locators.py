from selenium.webdriver.common.by import By

class MainPageLocators:
    marketplace_link = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(4) a')
    privacy_policy_link = (By.CSS_SELECTOR, 'div.section-content ul li:nth-child(2) a[href*="privacy-policy"]')
    telegram_link = (By.CSS_SELECTOR, 'div.social > a:nth-child(5)')
    blog = (By.CSS_SELECTOR, '#footer-website > div > div:nth-child(2) > div.footer-section.not-foldable > div > ul > li:nth-child(2) > a')

