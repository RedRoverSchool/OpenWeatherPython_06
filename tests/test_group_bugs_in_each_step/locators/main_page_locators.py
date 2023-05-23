from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    CURRENT_AND_FORECAST_APIS = (By.XPATH, "//a[text()='Current and Forecast APIs']")
    HISTORICAL_WEATHER_DATA_LINK = (By.XPATH, "//a[contains(text(), 'Historical Weather Data')]")
    WEATHER_DASHBOARD_LINK = (By.XPATH, "//a[contains(text(), 'Weather Dashboard')]")
    HOW_TO_START = (By.XPATH, "//div[@id='footer-website']//a[text()='How to start']")


