from selenium.webdriver.common.by import By

class MainPageLocators:
    HEADER_DASHBOARD_LINK = (By.XPATH, '//*[@id="desktop-menu"]/ul/li[3]/a')
    PRICING_AND_LIMITS_MODULE = [(By.XPATH, '//h2[text()="Pricing and limits"]'),
                                     (By.XPATH, '//html/body/main/div[2]/section/div/p'),
                                     (By.XPATH, '//html/body/main/div[2]/section/div/table')]