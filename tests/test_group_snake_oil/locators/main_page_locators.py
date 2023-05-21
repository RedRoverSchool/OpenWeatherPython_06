from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPageLocators:
    ALLOW_ALL_COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    LINKEDIN_ICON = (By.CSS_SELECTOR, "div[class='social'] a:nth-child(3)")
