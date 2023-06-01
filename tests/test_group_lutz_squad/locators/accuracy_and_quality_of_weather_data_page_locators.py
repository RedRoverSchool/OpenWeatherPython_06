from selenium.webdriver.common.by import By

class AccuracyAndQualityOfWeatherDataPageLocators:
    ACCURACY_AND_QUALITY_PAGE_LINK = "https://openweathermap.org/accuracy-and-quality"
    accuracy_and_quality_of_weather_data_link_locator = (By.CSS_SELECTOR, 'a[href*="/accuracy-and-quality"]')
    example_of_graphics_with_some_metrics_locator = (By.CSS_SELECTOR, 'img[src*="/themes/openweathermap/assets/img/accuracy_weather_data.png"]')
    number_of_cities_for_evaluation = (By.CSS_SELECTOR, ".col-sm-12 p>a")
