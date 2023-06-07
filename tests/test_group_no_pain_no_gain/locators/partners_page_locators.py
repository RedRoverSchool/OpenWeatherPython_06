from selenium.webdriver.common.by import By


class PartnersPageLocators:
    PARTNERS_PAGE_HEADING = (By.XPATH, '//h1')
    PARTNERS_PAGE_INFO_BOARD = (By.XPATH, "//div[@class='info-board info-board-orange']")
    RASPBERRY = (By.CSS_SELECTOR, '#raspberry > a')
    ANDROID_FIRST_LINK = (By.CSS_SELECTOR, '#android a[href*="/4-free-weather-providers-api-to-develop.html"]')
    INFO_BOARD_GITHUB_LINK = (By.XPATH, "//a[text()='GitHub']")
    MOBILE_APP_BLOCK = (By.CSS_SELECTOR, "#mobile > h2")
    MOBILE_APP_LINK = (By.XPATH, "//*[@id='mobile']/p/a")
