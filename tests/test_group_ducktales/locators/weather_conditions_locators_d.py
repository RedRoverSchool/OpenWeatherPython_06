from selenium.webdriver.common.by import By


class WeatherConditionsLocators:
    WEATHER_CONDITIONS_PAGE_URL = "https://openweathermap.org/weather-conditions"
    ELEMENTS_LOCATOR_CODES = lambda table: (By.XPATH, f"//table[@class='table table-bordered'][(position() = {table})]/tbody/tr/td[1]")
    ELEMENTS_LOCATOR_DESC = lambda table: (
    By.XPATH, f"//table[@class='table table-bordered'][(position() = {table})]/tbody/tr/td[3]")
