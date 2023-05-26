from selenium.webdriver.common.by import By


class AccuracyAndQualityPageLocators:
    ACCURACY_AND_QUALITY_PAGE_LINK = "https://openweathermap.org/accuracy-and-quality"
    number_of_cities_for_evaluation = (By.CSS_SELECTOR, ".col-sm-12 p>a")
