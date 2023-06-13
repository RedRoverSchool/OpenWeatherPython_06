from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPageLocators:
    ALLOW_ALL_COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    LINKEDIN_ICON = (By.CSS_SELECTOR, "div[class='social'] a:nth-child(3)")
    SUPPORT_DROPDOWN = (By.ID, "support-dropdown")
    FAQ_ELEMENT = (By.XPATH, "//*[@id='support-dropdown-menu']/li[1]/a")
    OVERLAY_LOCATOR = (By.CLASS_NAME, "owm-loader")
