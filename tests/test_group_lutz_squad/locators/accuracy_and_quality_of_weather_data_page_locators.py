from selenium.webdriver.common.by import By


class AccuracyAndQualityOfWeatherDataPageLocators:
    ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK_LOCATOR = (
    By.CSS_SELECTOR, 'a[href*="/accuracy-and-quality"]')
    EXAMPLE_OF_GRAPHICS_WITH_SOME_METRICS_LOCATOR = (By.CSS_SELECTOR, 'img[src*="/themes/openweathermap/assets/img/accuracy_weather_data.png"]')
