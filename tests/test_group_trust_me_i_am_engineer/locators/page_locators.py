from selenium.webdriver.common.by import By

class MainPageLocators:
    METRIC_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
    IMPERIAL_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
    CURRENT_TEMP = (By.CSS_SELECTOR, "div.current-temp span.heading")
    LOC_DATE_TIME = (By.XPATH, "//div[@class='current-container mobile-padding']/div/span[@class='orange-text']")

class WeatherAPIPageLocators:
    WEATHER_API_PAGE_TITLE = (By.CSS_SELECTOR, "h1.breadcrumb-title")

class MarketplacePageLocators:
    HISTORY_BILK_TITLE = (By.XPATH, "//h5/a[contains(text(), 'History Bulk')]")
    HISTORY_BILK_SEARCH_LOCATION = (By.ID, "firstSearch")
    BUTTON_SEARCH_METHODS = (By.XPATH, "//div[@class='search-pop-up']/button")