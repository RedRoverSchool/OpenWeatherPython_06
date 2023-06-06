from selenium.webdriver.common.by import By


class DashboardLocators:
    HEADER_DASHBOARD_LINK = "https://openweathermap.org/weather-dashboard/"
    HEADER_DASHBOARD = (By.XPATH, '//*[@id="desktop-menu"]/ul/li[3]/a')
    PRICING_PLANS_SUBSCRIBE = By.XPATH, '//tr[1]/th[3]/p/a'
    PRICING_PLANS_SUBSCRIBE1 = By.XPATH, '//tr[1]/th[4]/p/a'
    PRICING_PLANS_SUBSCRIBE2 = By.XPATH, '//tr[1]/th[5]/p/a'
    PRICING_PLANS_SUBSCRIBE3 = By.XPATH, '//tr[1]/th[6]/p/a'
    DASHBOARD_LOGO_IMAGE = (By.XPATH, '//html/body/main/div[2]/div[8]/div/div/div[2]/img')