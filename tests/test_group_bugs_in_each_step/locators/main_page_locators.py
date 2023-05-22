from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    HISTORICAL_WEATHER_DATA = (By.XPATH, "//a[contains(text(), 'Historical Weather Data')]")
    CURRENT_AND_FORECAST_APIS = (By.XPATH, "//a[text()='Current and Forecast APIs']")
