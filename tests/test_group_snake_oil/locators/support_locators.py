from selenium.webdriver.common.by import By


class SupportPageLocators:
    SUPPORT_DROPDOWN = (By.ID, "support-dropdown")
    FAQ_ELEMENT = (By.XPATH, "//*[@id='support-dropdown-menu']/li[1]/a")
    OVERLAY_LOCATOR = (By.CLASS_NAME, "owm-loader")
