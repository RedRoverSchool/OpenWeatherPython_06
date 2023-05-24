from selenium.webdriver.common.by import By


class AccuracyAndQualityOfWeatherDataPageLocators:
    accuracy_and_quality_of_weather_data_link_locator = (
    By.CSS_SELECTOR, '#footer-website > div > div:nth-child(2) > div:nth-child(1) > div > ul > li:nth-child(2) > a')
    example_of_graphics_with_some_metrics_locator = (By.CSS_SELECTOR, "body > main > div:nth-child(2) > div > div > div > img")
