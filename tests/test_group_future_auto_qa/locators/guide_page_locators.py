from selenium.webdriver.common.by import By


class GuidePageLocators:
    WEATHER_MAPS_COLLECTION_BLOCK = (By.CSS_SELECTOR, ".col-sm-12 ol ul:nth-of-type(3)")
    GLOBAL_PRECIPITATION_MAPS_LINK = (By.CSS_SELECTOR, "ul li:nth-child(2) a[href='/api/global-precipitation-map']")
