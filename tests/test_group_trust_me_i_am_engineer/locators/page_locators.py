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
    PRICING_PAGE_TITLE = (By.XPATH, "//h1[text()='Pricing']")
    FOR_BUSINESS_LINK = (By.XPATH, "//a[text()='OpenWeather for Business']")
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[@class ='stick-footer-panel__link']")
    ABOUT_US_BUTTON = (By.XPATH, "//a[@href='/about-us']")
    FOOTER_LINKEDIN_LINK = (By.XPATH, "//div[@class='social']/a[3]")


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
    BUTTON_IMPORT_CSV = (By.XPATH, "//button[contains(text(), 'Import CSV file')]")
    INPUT_FIELD_UPLOAD_FILE = (By.ID, "importCSV")
    DIV_FIELD_UPLOAD_FILE = (By.XPATH, "//*[@id='app']/div[2]/div")
    LOCATION_NAME_TABLE = (By.XPATH, "//table[@class='material-table']/tbody/tr/td[2]")
    LATITUDE_TABLE = (By.XPATH, "//table[@class='material-table']/tbody/tr/td[3]")
    LONGITUDE_TABLE = (By.XPATH, "//table[@class='material-table']/tbody/tr/td[4]")
    SATELLITE_BUTTON_LOC = (By.XPATH, "//div[@class='gm-style-mtc']/button[contains(text(), 'Satellite')]")
    CHECKBOX_TERRAIN = (By.XPATH, "//li[@aria-label='Terrain']/span/span[2]")
    BUTTON_ZOOM_IN = (By.XPATH, "//button[@title='Zoom in']")
    BUTTON_ZOOM_OUT = (By.XPATH, "//button[@title='Zoom out']")
    BUTTON_STREET_VIEW = (By.XPATH, "//button[@title='Drag Pegman onto the map to open Street View']")
    BUTTON_FULL_SCREEN = (By.XPATH, "//button[@title='Toggle fullscreen view']")

class WeatherConditionsLocators:
    ICON_LIST_DESCRIPTION = (By.XPATH, "//table[@class='table table-bordered'][1]/tbody/tr/td[3]")

class OurInitiativesPageLocators:
    OUR_INITIATIVES_LINK = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(7)')
    LEARN_MORE_LINK = (By.CSS_SELECTOR, 'a[class="ow-btn round btn-black"]')
    LEARN_MORE_PAGE_TITLE = (By.CSS_SELECTOR, "h1[class='breadcrumb-title']")
    HEADERS_SELECTOR = (By.XPATH, "//h2[@style='margin-top: 0;']")

class AboutUsPageLocators():
    HEADER = (By.XPATH, "//h1")
    IMAGE_BESIDE_HEADER = (By.CSS_SELECTOR, "img.tablet-plus")
    HEADERS_ON_PAGE_FOOTER = (By.XPATH, "//div[@class='horizontal-section']/div[not(contains(@class,'not-foldable'))]/p")
    NEWS_AND_UPDATES_BUTTON = (By.XPATH, "// div / a[contains( @ href, 'blog/category/weather')]")

class SubscriptionsPageLocators():
    BUTTON_CONTINUE_TO_PAYMENT = (By.XPATH, "//input[@value='Continue to payment']")
    RADIOBUTTON_ORGANISATIONS = (By.XPATH, "//span[2]//input[@type='radio']")
    ERROR_MESSAGE = (By.XPATH, "//span[@class='help-block']")

class PartnersPageLocators():
    BUTTON_VIEW_ON_GITHUB = (By.XPATH, "//a[@href='https://github.com/google/maps-for-work-samples/blob/master/samples/maps/OpenWeatherMapLayer/index.html']")
    BUTTON_OPEN_MANUAL = (By.XPATH, "//a[text()='Open manual']")
    BUTTON_SEE_ON_THE_WEBSITE = (By.XPATH, "//a[@href='http://drupal.org/project/olowm']")

class TechnologyPageLocators:
    DETAILED_REPORT_LINK = (By.XPATH, "//div[@class='container']//p[8]//a")

