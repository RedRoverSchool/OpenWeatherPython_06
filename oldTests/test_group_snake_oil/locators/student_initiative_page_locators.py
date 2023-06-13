from selenium.webdriver.common.by import By


class StudentInitiativePageLocators:
    LEARN_MORE_LINK_DEVELOPER_PLAN = (By.CSS_SELECTOR, "center>a[href='/price']")
    LEARN_MORE_LINK_MEDIUM_PLAN = (By.CSS_SELECTOR, "center>a[href='/price#history']")
