from selenium.webdriver.common.by import By


class HourlyForecastPageLocators:

    ALLOW_ALL_COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    CALL_HOURLY_FORECAST_DATA = (By.CSS_SELECTOR, "a[href='#5days']")
    HOW_TO_MAKE_AN_API_CALL = (By.CSS_SELECTOR, "a[href='#geo5']")
    WEATHER_FIELDS_IN_API_RESPONSE = (By.CSS_SELECTOR, "a[href='#parameter']")
    JSON = (By.CSS_SELECTOR, "a[href='#JSON']")
    XML = (By.CSS_SELECTOR, "a[href='#XML']")
    LIST_OF_CONDITION_CODES = (By.CSS_SELECTOR, "a[href='#list']")
    MIN_MAX_TEMPERATURE_IN_OUR_WEATHER_API = (By.CSS_SELECTOR, "a[href='#min']")
    OTHER_FEATURES = (By.CSS_SELECTOR, "a[href='#other']")
    GEOCODING_API = (By.CSS_SELECTOR, "a[href='#geocoding']")
    BUILT_IN_GEOCODING = (By.CSS_SELECTOR, "a[href='#builtin']")
    BUILT_IN_API_REQUEST_BY_CITY_NAME = (By.CSS_SELECTOR, "a[href='#name5']")
    BUILT_IN_API_REQUEST_BY_CITY_ID = (By.CSS_SELECTOR, "a[href='#cityid5']")
    BUILT_IN_API_REQUEST_BY_ZIP_CODE = (By.CSS_SELECTOR, "a[href='#zip']")
    FORMAT = (By.CSS_SELECTOR, "a[href='#format']")
    LIMITATION_OF_RESULT = (By.CSS_SELECTOR, "a[href='#limit']")
    UNITS_OF_MEASUREMENT = (By.CSS_SELECTOR, "a[href='#data']")
    MULTILINGUAL_SUPPORT = (By.CSS_SELECTOR, "a[href='#multi']")
    CALL_BACK_FUNCTION = (By.CSS_SELECTOR, "a[href='#call']")

    link_locators = [CALL_HOURLY_FORECAST_DATA, HOW_TO_MAKE_AN_API_CALL, WEATHER_FIELDS_IN_API_RESPONSE, JSON, XML,
                     LIST_OF_CONDITION_CODES, MIN_MAX_TEMPERATURE_IN_OUR_WEATHER_API, OTHER_FEATURES, GEOCODING_API,
                     BUILT_IN_GEOCODING, BUILT_IN_API_REQUEST_BY_CITY_NAME, BUILT_IN_API_REQUEST_BY_CITY_ID,
                     BUILT_IN_API_REQUEST_BY_ZIP_CODE, FORMAT, LIMITATION_OF_RESULT, UNITS_OF_MEASUREMENT,
                     MULTILINGUAL_SUPPORT, CALL_BACK_FUNCTION]
