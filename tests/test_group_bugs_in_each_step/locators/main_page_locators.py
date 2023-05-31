from selenium.webdriver.common.by import By


class MainPageLocators:
    ABOUT_US_LINK = (By.CSS_SELECTOR, ".not-foldable > .section-content > ul > :nth-child(1) > a")
    ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK = \
        (By.XPATH, "//a[contains(text(), 'Accuracy and quality of weather data')]")
    CONNECT_YOUR_WEATHER_STATION_LINK = (By.CSS_SELECTOR, "li a[href*='station']")
    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    CURRENT_AND_FORECAST_APIS = (By.XPATH, "//a[text()='Current and Forecast APIs']")
    HISTORICAL_WEATHER_DATA_LINK = (By.XPATH, "//a[contains(text(), 'Historical Weather Data')]")
    HOW_TO_START = (By.XPATH, "//div[@id='footer-website']//a[text()='How to start']")
    HOW_TO_START_LINK = (By.CSS_SELECTOR, "div[class='section-content'] a[href*='appid']")
    OPENWEATHER_FOR_BUSINESS_LINK = (By.CSS_SELECTOR, ".not-foldable > .section-content > ul > :nth-child(3) > a")
    OUR_TECHNOLOGY_LINK = (By.XPATH, "//a[contains(text(), 'Our technology')]")
    SUBSCRIBE_FOR_FREE_LINK = \
        (By.CSS_SELECTOR, ":nth-child(1) > :nth-child(2) > .section-content > ul > :nth-child(3) > a")
    WEATHER_MAPS_LINK = (By.XPATH, "//a[contains(text(), 'Weather Maps')]")
    WEATHER_DASHBOARD_LINK = (By.XPATH, "//a[contains(text(), 'Weather Dashboard')]")

