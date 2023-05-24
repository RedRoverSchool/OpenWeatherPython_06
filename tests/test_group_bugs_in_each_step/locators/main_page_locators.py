from selenium.webdriver.common.by import By


class MainPageLocators:

    ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK = (By.XPATH, "//a[contains(text(), 'Accuracy and quality of weather data')]")
    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    CURRENT_AND_FORECAST_APIS = (By.XPATH, "//a[text()='Current and Forecast APIs']")
    HISTORICAL_WEATHER_DATA_LINK = (By.XPATH, "//a[contains(text(), 'Historical Weather Data')]")
    HOW_TO_START = (By.XPATH, "//div[@id='footer-website']//a[text()='How to start']")
    OUR_TECHNOLOGY_LINK = (By.XPATH, "//a[contains(text(), 'Our technology')]")
    WEATHER_MAPS_LINK = (By.XPATH, "//a[contains(text(), 'Weather Maps')]")
    WEATHER_DASHBOARD_LINK = (By.XPATH, "//a[contains(text(), 'Weather Dashboard')]")

