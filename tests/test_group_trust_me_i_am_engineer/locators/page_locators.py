from selenium.webdriver.common.by import By

class MainPageLocators:
    METRIC_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
    IMPERIAL_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
    CURRENT_TEMP = (By.CSS_SELECTOR, "div.current-temp span.heading")
    LOC_DATE_TIME = (By.XPATH, "//div[@class='current-container mobile-padding']/div/span[@class='orange-text']")
    CITY_NAME = (By.CSS_SELECTOR, "div.current-container.mobile-padding div h2")
    LOC = (By.CSS_SELECTOR, "div.control-el svg.icon-current-location")
    LOAD_DIV = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
    FOOTER_PRICING_LINK = (By.XPATH, "//div[@class='inner-footer-container']//a[text()='Pricing']")
    SEARCH_CITY_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Search city"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class ="button-round dark"]')
    SEARCH_OPTION_FROM_DROPDOWN_LIST = (By.XPATH, "//span[contains(text(), city)]")
    WEEKDAY_IN_8_DAYS_FORECAST = (By.XPATH, "//div//li[@data-v-5ed3171e]/span")

class WeatherAPIPageLocators:
    WEATHER_API_PAGE_TITLE = (By.CSS_SELECTOR, "h1.breadcrumb-title")

class MarketplacePageLocators:
    HISTORY_BULK_TITLE = (By.XPATH, "//h5/a[contains(text(), 'History Bulk')]")
    HISTORY_BULK_SEARCH_LOCATION = (By.ID, "firstSearch")
    BUTTON_SEARCH_METHODS = (By.XPATH, "//div[@class='search-pop-up']/button")
    MAP_BUTTON_LOC = (By.XPATH, "//div[@class='gm-style-mtc']/button[contains(text(), 'Map')]")
    BUTTON_BY_LOCATION = (By.XPATH, "//button[contains(text(), 'By location')]")
    BUTTON_BY_COORDINATES = (By.XPATH, "//button[contains(text(), 'By coordinates')]")
    FIRST_SEARCH_ITEMS = (By.XPATH, "/html/body/div[4]/div[1]/span[2]/span")
    SEARCH_POP_UP_HEADER = (By.XPATH, "//div[@class='pop-up-marker']/div[@class='pop-up-header']/h3")
    INPUT_LATITUDE = (By.XPATH, "//input[@placeholder='Latitude']")
    INPUT_LONGITUDE = (By.XPATH, "//input[@placeholder='Longitude']")
    LATITUDE_ON_MAP = (By.XPATH, "//div[@class='text']/p[1]")
    LONGITUDE_ON_MAP = (By.XPATH, "//div[@class='text']/p[2]")

class WeatherConditionsLocators:
    ICON_LIST_DESCRIPTION = (By.XPATH, "//table[@class='table table-bordered'][1]/tbody/tr/td[3]")

