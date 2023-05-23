from selenium.webdriver.common.by import By


class EightDayForecast:
    URL = 'https://openweathermap.org'
    SEARCH_SKY_IN_WORDS = (By.XPATH, "//div[@class='day-list-values']/span[contains(@class,'sub')]")
