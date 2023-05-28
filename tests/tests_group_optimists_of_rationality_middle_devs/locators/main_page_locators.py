from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_DASHBOARD_LINK = (By.XPATH, '//*[@id="desktop-menu"]/ul/li[3]/a')
    PRICING_AND_LIMITS_MODULE = [(By.XPATH, '//h2[text()="Pricing and limits"]'),
                                 (By.XPATH, '//html/body/main/div[2]/section/div/p'),
                                 (By.XPATH, '//html/body/main/div[2]/section/div/table')]
    DASHBOARD_LOGO_IMAGE = (By.XPATH, '/html/body/main/div[2]/div[8]/div/div/div[2]/img')
    PRICING_AND_LIMITS_MODULE = [(By.XPATH, '//h2[text()="Pricing and limits"]'),
                                 (By.XPATH, '//html/body/main/div[2]/section/div/p'),
                                 (By.XPATH, '//html/body/main/div[2]/section/div/table')]
    PRICING_PLANS_SIGN_UP = (By.XPATH, "//a[text()='Sign Up']")