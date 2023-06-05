from selenium.webdriver.common.by import By


class GuidePageLocators:
    GUIDE_PAGE_LINK = 'https://openweathermap.org/guide'
    INDUSTRY_APIS_LOCATOR = (By.XPATH, "//*[contains(text(),'industry standard APIs')]")
    ONE_CALL_API_BY_CALL_LOCATOR = (By.XPATH, "//*[text()='One Call API by call']")
    SUBSCRIBE_TO_ONE_CALL_BY_CALL_BUTTON = (By.CSS_SELECTOR, "a[href='/price'].ow-btn.round.btn-orange")
