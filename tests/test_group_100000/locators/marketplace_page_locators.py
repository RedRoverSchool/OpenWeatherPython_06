from selenium.webdriver.common.by import By


class MarketplaceLocators:
    URL_HISTORICAL_WEATHER = 'https://home.openweathermap.org/zip_code_data/new'
    SELECT_STATE_FIELD = (By.CSS_SELECTOR, '#__BVID__10 .form-control.dropdown-selector')
    STATE_TEXAS = (By.XPATH, "//span[text()='Texas']")
    SELECT_YEAR_FIELD = (By.CSS_SELECTOR, "#__BVID__13 .form-control.dropdown-selector")
    YEAR_2019 = (By.CSS_SELECTOR, "#__BVID__13 li:last-child")
    EXPECTED_YEAR = (By.CSS_SELECTOR, "#__BVID__13 .res")
    WEATHER_PAR_LIST = (By.XPATH, "//*[@class='section']//ul[@class='owm-list']/li")
    UNITS_INFO = (By.XPATH, "//div[@class='filters']//span[2]")

