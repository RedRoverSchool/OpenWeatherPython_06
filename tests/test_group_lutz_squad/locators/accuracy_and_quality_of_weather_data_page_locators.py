from selenium.webdriver.common.by import By


class AccuracyAndQualityOfWeatherDataPageLocators:
    accuracy_and_quality_of_weather_data_link_locator = (
    By.CSS_SELECTOR, 'a[href*="/accuracy-and-quality"]')
    example_of_graphics_with_some_metrics_locator = (By.CSS_SELECTOR, 'img[src*="/themes/openweathermap/assets/img/accuracy_weather_data.png"]')
