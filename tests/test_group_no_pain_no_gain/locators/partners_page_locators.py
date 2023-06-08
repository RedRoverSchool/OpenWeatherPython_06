from selenium.webdriver.common.by import By


class PartnersPageLocators:
    PARTNERS_PAGE_HEADING = (By.XPATH, '//h1')
    PARTNERS_PAGE_INFO_BOARD = (By.XPATH, "//div[@class='info-board info-board-orange']")
    RASPBERRY = (By.CSS_SELECTOR, '#raspberry > a')
    ANDROID_FIRST_LINK = (By.CSS_SELECTOR, '#android a[href*="/4-free-weather-providers-api-to-develop.html"]')
    INFO_BOARD_GITHUB_LINK = (By.XPATH, "//a[text()='GitHub']")
    MOBILE_APP_BLOCK = (By.CSS_SELECTOR, "#mobile > h2")
    MOBILE_APP_LINK = (By.XPATH, "//*[@id='mobile']/p/a")
    GOOGLE_01 = (By.XPATH, "(//div[@class='doc-container']//li/a)[1]")
    GOOGLE_02 = (By.XPATH, "(//div[@class='doc-container']//li/a)[2]")
    MOZILLA = (By.XPATH, "(//div[@class='doc-container']//li/a)[3]")
    UBUNTU = (By.XPATH, "(//div[@class='doc-container']//li/a)[4]")
    ANDROID = (By.XPATH, "(//div[@class='doc-container']//li/a)[5]")
    LEAFLET = (By.XPATH, "(//div[@class='doc-container']//li/a)[6]")
    JAVA = (By.XPATH, "(//div[@class='doc-container']//li/a)[7]")
    GO = (By.XPATH, "(//div[@class='doc-container']//li/a)[8]")
    JS = (By.XPATH, "(//div[@class='doc-container']//li/a)[9]")
    CMS = (By.XPATH, "(//div[@class='doc-container']//li/a)[10]")
    RASPBERRY_ANCHOR = (By.XPATH, "(//div[@class='doc-container']//li/a)[11]")
    PYTHON = (By.XPATH, "(//div[@class='doc-container']//li/a)[12]")
    PHP = (By.XPATH, "(//div[@class='doc-container']//li/a)[13]")
    APACHE = (By.XPATH, "(//div[@class='doc-container']//li/a)[14]")
    DESKTOP = (By.XPATH, "(//div[@class='doc-container']//li/a)[15]")
    MOBILE_APP = (By.XPATH, "(//div[@class='doc-container']//li/a)[16]")
    BIG_LIBRARY = (By.XPATH, "(//div[@class='doc-container']//li/a)[17]")
    ANCHOR_LOCATORS = [
        GOOGLE_01, GOOGLE_02, MOZILLA, UBUNTU, ANDROID, LEAFLET, JAVA,
        GO, JS, CMS, RASPBERRY_ANCHOR, PYTHON, PHP, APACHE, DESKTOP, MOBILE_APP, BIG_LIBRARY
    ]
