from selenium.webdriver.common.by import By


class SupportPageLocators:
    Support_dropdown = (By.ID, "support-dropdown")
    FAQ_element = (By.XPATH, "//*[@id='support-dropdown-menu']/li[1]/a")
