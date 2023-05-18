from selenium.webdriver.common.by import By

class MainPageLocators:
    METRIC_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
    IMPERIAL_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
    CURRENT_TEMP = (By.CSS_SELECTOR, "div.current-temp span.heading")

class WeatherAPIPageLocators:
    WEATHER_API_PAGE_TITLE = (By.CSS_SELECTOR, "h1.breadcrumb-title")

class MarketplacePageLocators:
    pass