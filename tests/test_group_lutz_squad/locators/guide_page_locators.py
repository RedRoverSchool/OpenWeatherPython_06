from selenium.webdriver.common.by import By


class GuidePageLocators:
    GUIDE_PAGE_LINK = 'https://openweathermap.org/guide'
    INDUSTRY_APIS_LOCATOR = (By.XPATH, "//*[contains(text(),'industry standard APIs')]")
