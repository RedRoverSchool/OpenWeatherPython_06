from selenium.webdriver.common.by import By


class MarketplaceLocators:
    URL_HISTORICAL_WEATHER = 'https://home.openweathermap.org/zip_code_data/new'
    SELECT_STATE_FIELD = (By.CSS_SELECTOR, '#__BVID__10 .form-control.dropdown-selector')
    STATE_TEXAS = (By.XPATH, "//span[text()='Texas']")
    SELECT_YEAR_FIELD = (By.CSS_SELECTOR, "#__BVID__13 .form-control.dropdown-selector")
    YEAR_2019 = (By.CSS_SELECTOR, "#__BVID__13 li:last-child")
    EXPECTED_YEAR = (By.CSS_SELECTOR, "#__BVID__13 .res")
    WEATHER_PAR_LIST = (By.XPATH, "//*[@class='section']//ul[@class='owm-list']/li")
    UNITS_INFO = (By.XPATH, "//div[@class='filters']/p[1]/span[2]")
    FILE_FORMAT_INFO = (By.XPATH, "//div[@class='filters']/p[2]/span[2]")
    STATE_TEXAS_SUB = (By.XPATH, "//span[text()='Texas']/following-sibling::*")
    TOTAL_AMOUNT = (By.CSS_SELECTOR, ".footer-content>h4")
    URL_HISTORY_FORECAST_BULK = 'https://home.openweathermap.org/history_forecast_bulks/new'
    SEARCH_FLD = (By.CSS_SELECTOR, "#firstSearch")
    BY_LOCATION_BTN = (By.CSS_SELECTOR, "div .search-pop-up > button:first-child")
    CITY_NAME_FROM_DROPDOWN_MENU = (By.CSS_SELECTOR, "div .pac-item:first-child")
    CITY_NAME_ON_MAP = (By.CSS_SELECTOR, "div .pop-up-marker .pop-up-header >h3")
    REQUESTED_CITY = "Paris"