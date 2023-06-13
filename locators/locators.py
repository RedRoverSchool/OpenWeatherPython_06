from selenium.webdriver.common.by import By


class BasePageLocators:
    SIGN_IN_LINK = (By.CSS_SELECTOR, '.user-li a')
    GUIDE_LINK = (By.CSS_SELECTOR, "#desktop-menu a[href*='guide']")
    DASHBOARD_LINK = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
    PRICING_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, 'div.section-content ul li:nth-child(2) a[href*="privacy-policy"]')
    OUR_INITIATIVES_LINK = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(7) a')
    PARTNERS_LINK = (By.CSS_SELECTOR, '#desktop-menu a[href="/examples"]')
    SUPPORT_LINK = (By.XPATH, "//*[@id='support-dropdown']")
    FAQ_OPTION = (By.XPATH, "//*[@id='support-dropdown-menu']//a[@href='/faq']")
    MAPS_LINK = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(6) a')
    HOW_TO_START_OPTION = (By.XPATH, "//*[@id='support-dropdown-menu']//a[@href='/appid']")
    ASK_A_QUESTION_OPTION = (
        By.XPATH, "//*[@id='support-dropdown-menu']//a[@href='https://home.openweathermap.org/questions']")
    API_LINK = (By.CSS_SELECTOR, "#desktop-menu a[href*='api']")
    DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
    HEADER = (By.XPATH, "//h1")
    GLOBAL_WEATHER_ALERTS_LINK = "https://openweathermap.org/api/push-weather-alerts"
    LOGO_LOCATOR = (By.CSS_SELECTOR, ".logo > a > img")


class MainPageLocators:
    ABOUT_US_LINK = (By.CSS_SELECTOR, ".not-foldable > .section-content > ul > :nth-child(1) > a")
    ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK = \
        (By.XPATH, "//a[contains(text(), 'Accuracy and quality of weather data')]")
    CONNECT_YOUR_WEATHER_STATION_LINK = (By.CSS_SELECTOR, "li a[href*='station']")
    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    HISTORICAL_WEATHER_DATA_LINK = (By.XPATH, "//a[contains(text(), 'Historical Weather Data')]")
    HOW_TO_START = (By.XPATH, "//div[@id='footer-website']//a[text()='How to start']")
    HOW_TO_START_LINK = (By.CSS_SELECTOR, "div[class='section-content'] a[href*='appid']")
    OPENWEATHER_FOR_BUSINESS_LINK = (By.CSS_SELECTOR, ".not-foldable > .section-content > ul > :nth-child(3) > a")
    OUR_TECHNOLOGY_LINK = (By.XPATH, "//a[contains(text(), 'Our technology')]")
    PRODUCT_COLLECTIONS = (By.XPATH, "//p[@class='section-heading' and text()='Product Collections']")
    SUBSCRIBE_FOR_FREE_LINK = \
        (By.CSS_SELECTOR, ":nth-child(1) > :nth-child(2) > .section-content > ul > :nth-child(3) > a")
    WEATHER_DASHBOARD_LINK = (By.XPATH, "//a[contains(text(), 'Weather Dashboard')]")
    WEATHER_MAPS_LINK = (By.XPATH, "//a[contains(text(), 'Weather Maps')]")
    WEBSITE_TERMS_AND_CONDITIONS_LINK = (By.XPATH, "//a[contains(text(), 'Website')]")

    SEARCH_DROPDOWN = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
    SEARCH_DROPDOWN_OPTION = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    SEARCH_CITY_FIELD = (By.CSS_SELECTOR, "input[placeholder='Search city']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[class ='button-round dark']")
    DISPLAYED_CITY = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
    NO_RESULTS_NOTIFICATION = (By.CSS_SELECTOR, '.widget-notification > span')
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    MANAGE_COOKIES_BTN = (By.XPATH, '//*[@id="stick-footer-panel"]//a')
    ABOUT_US_BUTTON = (By.XPATH, "//a[@href='/about-us']")
    C_TEMP_LOCATOR = (By.CSS_SELECTOR, '.switch-container .option:nth-child(2)')
    LINE_IN_8_DAYS_FORECAST_LOCATOR = (By.XPATH, "//div[@class='day-list-values']/div/span[contains(text(), '°C')]")
    AGRICULTURE_ANALYTICS_TITLE_LOCATOR = (By.CSS_SELECTOR, ".section-content > .mobile-padding > div > h2")
    HEADER_SEARCH_FIELD = (By.NAME, "q")
    CURRENT_AND_FORECAST_APIS = (By.XPATH, "//a[text()='Current and Forecast APIs']")
    WIDGETS = (By.XPATH, "//a[text()='Widgets']")
    CHART_WEATHER = (By.CSS_SELECTOR, "canvas[id='chart-component']")
    XPATH_PRIVACY_POLICY_BUTTON = (By.XPATH, '//*[@id="footer-website"]/div/div[2]/div[2]/div/ul/li[2]/a')

    SUPPORT_MENU = (By.CSS_SELECTOR, '#support-dropdown')
    SUPPORT_FAQ_SUBMENU = (By.CSS_SELECTOR, '#support-dropdown-menu > li:nth-child(1) > a[href="/faq"]')
    chart_weather = (By.XPATH, "//*[@id='chart-component']")
    product_collection = [CURRENT_AND_FORECAST_APIS, HISTORICAL_WEATHER_DATA_LINK, WEATHER_MAPS_LINK,
                          WEATHER_DASHBOARD_LINK, WIDGETS]

    METRIC_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
    IMPERIAL_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
    CURRENT_TEMP = (By.CSS_SELECTOR, "div.current-temp span.heading")
    LOC_DATE_TIME = (By.XPATH, "//div[@class='current-container mobile-padding']/div/span[@class='orange-text']")
    CITY_NAME = (By.CSS_SELECTOR, "div.current-container.mobile-padding div h2")
    LOC = (By.CSS_SELECTOR, "div.control-el svg.icon-current-location")
    LOAD_DIV = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
    INITIATIVES = By.CSS_SELECTOR, "ul[id='first-level-nav'] li:nth-child(7) a:nth-child(1)"
    sections = ["Education", "Healthcare", "Open Source", "Weather stations"]
    section_locator = lambda section: (By.XPATH, f"//span[contains(text(), '{section}')]")
    QUESTION_XPATH = "//*[@id='faq']/div[{i}]/p"
    EDUCATION_SECTION_PAGE = "https://openweathermap.org/our-initiatives/student-initiative"
    EDUCATION_LEARN_MORE = By.CSS_SELECTOR, ".ow-btn.round.btn-black"
    MODULE_DOWNLOAD_OPENWEATHER_APP = (By.XPATH, "//div[@class='my-5']/p")
    FIRST_DAY_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'ul.day-list li:nth-child(1) span:nth-child(1)'
    LIST_DAYS_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'div .day-list'
    DAYS_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'div .day-list li'
    DAYS_IN_8_DAY_FORECAST_NUM = By.CSS_SELECTOR, 'div .day-list li span:nth-child(1)'
    APP_STORE_BRAND_LINK = By.CSS_SELECTOR, "img[src='/themes/openweathermap/assets/img/mobile_app/app-store-badge.svg']"
    GOOGLE_PLAY_BRAND_LINK = By.CSS_SELECTOR, "img[alt='Get it on Google Play']"
    FIELD_WEATHER_IN_YUOR_CITY = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")
    NWP_MODEL = (By.CSS_SELECTOR, ".col-sm-12 > ul:first-of-type")
    ASK_A_QUESTION_LINK = (By.XPATH, "(//*[contains(text(),'question')])[3]")

class DashboardPageLocators:
    HEADER_DASHBOARD_LINK = "https://openweathermap.org/weather-dashboard/"
    HEADER_DASHBOARD = (By.XPATH, '//*[@id="desktop-menu"]/ul/li[3]/a')
    PRICING_PLANS_SUBSCRIBE = (By.XPATH, '//tr[1]/th[3]/p/a')
    PRICING_PLANS_SUBSCRIBE1 = (By.XPATH, '//tr[1]/th[4]/p/a')
    PRICING_PLANS_SUBSCRIBE2 = (By.XPATH, '//tr[1]/th[5]/p/a')
    PRICING_PLANS_SUBSCRIBE3 = (By.XPATH, '//tr[1]/th[6]/p/a')
    DASHBOARD_LOGO_IMAGE = (By.XPATH, '//html/body/main/div[2]/div[8]/div/div/div[2]/img')
    PRICING_AND_LIMITS = (By.XPATH, '//h2[text()="Pricing and limits"]')
    PRICING_AND_LIMITS1 = (By.XPATH, '//html/body/main/div[2]/section/div/p')
    PRICING_AND_LIMITS2 = (By.XPATH, '//html/body/main/div[2]/section/div/table')
    BTN_DASHBOARD = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
    TITLE_HOW_TO_START = (By.XPATH, "//div/h2[contains(text(),'How to Start')]")
    TRY_THE_DASHBOARD2_BTN = (By.XPATH, "//div[6]//a[text()='Try the Dashboard']")
    PANEL_SIGN_IN_FORM = (By.CSS_SELECTOR, '.col-md-6 .panel-heading')
    WEATHER_SYMBOL = (By.CSS_SELECTOR, "ul  > li:nth-child(3) > span.symbol")
    PRICING_PLANS_SIGN_UP = (By.XPATH, "//a[text()='Sign Up']")
    IMAGE_LOCATOR = (By.XPATH, "//*[@class='responsive']")


class PricingPageLocators:
    URL_PRICING = 'https://openweathermap.org/price'
    LINK_TEXT_ONE_CALL = (By.CSS_SELECTOR, "#onecall > div > div > h2")
    button_detailed_pricing_locators = [(By.XPATH, '//*[@id="current"]//a[2]'),
                                        (By.XPATH, '//*[@id="history"]//a[2]')]


class ApiPageLocators:
    API_PAGE = 'https://openweathermap.org/api'
    button_weather_alerts_api_doc = (By.XPATH, "//*[@id='current']//a[@href='/api/push-weather-alerts']")
    actual_title_features = (By.XPATH, "//*[@id='about']/h2")
    button_get_access = 'href="mailto:info@openweathermap.org"'
    button_history_api_full_archive = (By.XPATH, "//*[@id='history']//*[@href='/api/history-api-full-archive']")
    ONE_CALL_API_LINK = 'https://openweathermap.org/api/one-call-3'
    ONE_CALL_API_3 = (By.CSS_SELECTOR, ".col-sm-6>h2>a[href ='/api/one-call-3']")
    DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
    GLOBAL_WEATHER_ALERTS_LINK = "https://openweathermap.org/api/push-weather-alerts"

class AboutUsPageLocators:
    HEADER = (By.XPATH, "//h1")
    IMAGE_BESIDE_HEADER = (By.CSS_SELECTOR, "img.tablet-plus")
    HEADERS_ON_PAGE_FOOTER = (
        By.XPATH, "//div[@class='horizontal-section']/div[not(contains(@class,'not-foldable'))]/p")
    NEWS_AND_UPDATES_BUTTON = (By.XPATH, "// div / a[contains( @ href, 'blog/category/weather')]")
    APP_STORE_BUTTON = (By.XPATH, "//a[contains(@href, 'app/openweather')]/img")
    BYU_BY_SUBSCRIPTIONS = (By.XPATH, "//a[contains(@href, 'subscriptions')]")
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, 'div.contact-us.blue-transparent-container.white-text a')
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    UBUNTU_MY_WEATHER_INDICATOR = (By.CSS_SELECTOR, "#ubuntu > a:nth-child(3)")


class AppStorePageLocators:
    APP_TITLE = (By.XPATH, "//h1")


class OpenAgroLocators:
    REQUEST_DATA_LOCATORS = (By.XPATH, '//a[text()="Request data"]')
    REQUEST_DATA_BUTTON = (By.CSS_SELECTOR, ".open-agro-banner__actions a")


class SolarApiLocators:
    HOW_TO_GET_ACCESS_LINK = (By.XPATH, '//a[@href="#how"]')
    HOW_TO_GET_ACCESS_TITLE = (By.CSS_SELECTOR, "#how h2")
    PRODUCT_CONCEPT_TITLE = (By.CSS_SELECTOR, "#concept h2")


class ApiKeysLocator:
    API_KEY_NAME_URL = 'https://home.openweathermap.org/api_keys'
    API_KEY_EDIT_SELECTOR = By.CSS_SELECTOR, "i[class='fa fa-edit']"
    API_KEY_NAME_SELECTOR = By.XPATH, "//table/tbody/tr/td[2]"
    API_KEY_ENTER_SELECTOR = By.CSS_SELECTOR, "input[name='edit_key_form[name]']"
    SAVE_BUTTON_SELECTOR = By.CSS_SELECTOR, "button[class='button-round dark']"
    TAB_API_KEYS = By.CSS_SELECTOR, '#myTab [href="/api_keys"]'
    MODULE_API_KEY_CREATE = By.CSS_SELECTOR, '.col-md-4 h4'
    EDIT_API_KEY_ICON = By.CSS_SELECTOR, '.edit_key_btn .fa-edit'
    API_KEY_FIELD = (By.CSS_SELECTOR, '#new_edit_key_form .owm_input')
    SAVE_NEW_API_NAME_BUTTON = By.CSS_SELECTOR, '.pop-up-footer .button-round.dark'
    API_KEY_NAME_FIRST_ROW = By.XPATH, "//div[@class='col-md-8']//tr[1]//td[2]"
    NEW_API_KEY_NAME = By.CSS_SELECTOR, ".new_api_key_form .owm_input"
    GENERATE_BUTTON = By.CSS_SELECTOR, '.new_api_key_form .button-round.dark'
    TABLE_API_KEYS = By.CSS_SELECTOR, "tbody tr"


class SignInPageLocators:
    CREATE_AN_ACCOUNT_LINK = (By.CSS_SELECTOR, ".sign-form > :nth-child(4) > a")
    REGISTRATION_QUESTION = By.XPATH, "//p[contains(text(), 'Not registered?')]"
    REGISTRATION_FORM_DISPLAY = (By.CSS_SELECTOR, ".sign-form")
    EMAIL_FIELD_DISPLAY = (By.CSS_SELECTOR, ".new_user > :nth-child(3)")
    PASSWORD_FIELD_DISPLAY = (By.CSS_SELECTOR, "#user_password")
    REMEMBER_ME_RECORD_DISPLAY = (By.CSS_SELECTOR, "label.boolean")
    CHECKBOX_DISPLAY = (By.CSS_SELECTOR, "#user_remember_me")
    SUBMIT_BUTTON_DISPLAY = (By.CSS_SELECTOR, ".new_user > .btn")
    LINK_FOR_PASSWORD_RECOVERY_DISPLAY = (By.CSS_SELECTOR, ".pwd-lost-q > a")


class SignInLocator:
    EMAIL_INPUT = By.CSS_SELECTOR, '#user_email'
    PASSWORD_INPUT = By.CSS_SELECTOR, '#user_password'
    SUBMIT_BUTTON = By.CSS_SELECTOR, "input[value='Submit']"
    ERROR_LOGIN_MESSAGE_DIV = (By.CSS_SELECTOR, '.panel.panel-red')
    SUCCESS_LOGIN_MESSAGE_DIV = By.CSS_SELECTOR, '.panel.panel-green'

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
    PLACE_ORDER_BTN = (By.CSS_SELECTOR, '.footer-content .orange-button-square')
    ADD_LOCATION_BTN = (By.CSS_SELECTOR, "button.button-round.dark:nth-child(2)")
    HISTORY_BULK_TITLE = (By.XPATH, "//h5/a[contains(text(), 'History Bulk')]")
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
    CHECKBOX_LABELS = (By.XPATH, "//li[@aria-label='Labels']/span")
    BUTTON_ZOOM_IN = (By.XPATH, "//button[@title='Zoom in']")
    BUTTON_ZOOM_OUT = (By.XPATH, "//button[@title='Zoom out']")
    BUTTON_STREET_VIEW = (By.XPATH, "//button[@title='Drag Pegman onto the map to open Street View']")
    BUTTON_FULL_SCREEN = (By.XPATH, "//button[@title='Toggle fullscreen view']")
    LST_NAME_CITY = (By.XPATH, "//*[contains(text(), 'Paris')]")
    LST_LATITUDE_COORDINATE = (By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[3]')
    LST_LONGITUDE_COORDINATE = (By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[4]')

class WeatherConditionsLocators:
    WEATHER_ICONS = (By.XPATH, '//a[.="Weather icons"]')
    ICONS_FOR_NIGHT_TIME = (By.XPATH, '//td[contains(text(), "n.png")]')

class GuideLocators:
    GUIDE_URL = 'https://openweathermap.org/guide'
    guide_fast_way_links_locators = [(By.XPATH, '//*[@class="lead"]//*[@href="https://openweather.co.uk/"]'),
                                     (By.XPATH, '//p[2]//*[@href="/api"]'),
                                     (By.XPATH, '//p[2]//*[@href="/api/road-risk"]'),
                                     (By.XPATH, '//p[2]//*[@href="/api/solar-energy-prediction"]')]
    NWP_MODEL = (By.CSS_SELECTOR, ".col-sm-12 > ul:first-of-type")
    TITLE_NWP_MODEL_LOCATOR = (By.CSS_SELECTOR, '.col-sm-12 ol h2:nth-of-type(2)')
    HISTORICAL_COLLECTION_LINKS = (By.CSS_SELECTOR, ".col-sm-12 ol ul:nth-of-type(2) a")
    HISTORICAL_COLLECTION_MODULE = (By.CSS_SELECTOR, ".col-sm-12 ol ul:nth-of-type(2)")
    LINK_HISTORICAL_ARCHIVE = (By.PARTIAL_LINK_TEXT, "archive")
    CLICK_ALLOW_IN_STICK_FOOTER = (By.CLASS_NAME, 'stick-footer-panel__link')

class PartnersLocators:
    APACHE_CAMEL_BUTTON = (By.CSS_SELECTOR, 'a[href*="camel.apache"]')
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    GIT_BUTTON_PHP = (By.CSS_SELECTOR, 'a[href*="php"]')
    GIT_BUTTON_PYTHON = (By.CSS_SELECTOR, 'a[href*="github.com/csparpa/pyowm"]')
    UBUNTU_MY_WEATHER_INDICATOR = (By.CSS_SELECTOR, "#ubuntu > a:nth-child(3)")
    BUTTON_VIEW_ON_GITHUB = (By.XPATH,
                             "//a[@href='https://github.com/google/maps-for-work-samples/blob/master/samples/maps/OpenWeatherMapLayer/index.html']")
    BUTTON_OPEN_MANUAL = (By.XPATH, "//a[text()='Open manual']")
    HEADERS_ON_THE_PAGE = (By.XPATH, "//h2")
    PARTNERS_PAGE_HEADING = (By.XPATH, '//h1')
    PARTNERS_PAGE_INFO_BOARD = (By.XPATH, "//div[@class='info-board info-board-orange']")
    RASPBERRY = (By.CSS_SELECTOR, '#raspberry > a')
    ANDROID_FIRST_LINK = (By.CSS_SELECTOR, '#android a[href*="/4-free-weather-providers-api-to-develop.html"]')
    INFO_BOARD_GITHUB_LINK = (By.XPATH, "//a[text()='GitHub']")
    MOBILE_APP_BLOCK = (By.CSS_SELECTOR, "#mobile > h2")
    MOBILE_APP_LINK = (By.XPATH, "//*[@id='mobile']/p/a")
    GOOGLE_01 = (By.XPATH, "(//div[@class='doc-container']//li/a)[1]")
    GOOGLE_02 = (By.XPATH, "(//div[@class='doc-container']//li/a)[2]")
    MOZILLA = (By.XPATH, "(//div[@class='doc-container']//li/a)[3]")
    UBUNTU = (By.XPATH, "(//div[@class='doc-container']//li/a)[4]")
    ANDROID = (By.XPATH, "(//div[@class='doc-container']//li/a)[5]")
    LEAFLET = (By.XPATH, "(//div[@class='doc-container']//li/a)[6]")
    JAVA = (By.XPATH, "(//div[@class='doc-container']//li/a)[7]")
    GO = (By.XPATH, "(//div[@class='doc-container']//li/a)[8]")
    JS = (By.XPATH, "(//div[@class='doc-container']//li/a)[9]")
    CMS = (By.XPATH, "(//div[@class='doc-container']//li/a)[10]")
    RASPBERRY_ANCHOR = (By.XPATH, "(//div[@class='doc-container']//li/a)[11]")
    PYTHON = (By.XPATH, "(//div[@class='doc-container']//li/a)[12]")
    PHP = (By.XPATH, "(//div[@class='doc-container']//li/a)[13]")
    APACHE = (By.XPATH, "(//div[@class='doc-container']//li/a)[14]")
    DESKTOP = (By.XPATH, "(//div[@class='doc-container']//li/a)[15]")
    MOBILE_APP = (By.XPATH, "(//div[@class='doc-container']//li/a)[16]")
    BIG_LIBRARY = (By.XPATH, "(//div[@class='doc-container']//li/a)[17]")
    ANCHOR_LOCATORS = [
        GOOGLE_01, GOOGLE_02, MOZILLA, UBUNTU, ANDROID, LEAFLET, JAVA,
        GO, JS, CMS, RASPBERRY_ANCHOR, PYTHON, PHP, APACHE, DESKTOP, MOBILE_APP, BIG_LIBRARY
    ]
    LINK_SEE_LIBRARY = (By.XPATH, '//a[text()="See library"]')


class WidgetsConstractorLocators:
    FAHRENHEIT_BUTTON = (By.CSS_SELECTOR, 'span#imperial')
    CELSIUS_BUTTON = (By.CSS_SELECTOR, 'span#metric')


class RoadRiskApiLocators:
    ROAD_RISK_API_LINK = 'https://openweathermap.org/api/road-risk'
    LINK_API_KEYS = 'https://home.openweathermap.org/api_keys'
    TITLE_HOW_TO_RR_API = (By.XPATH, "//*[@id='how']/h2")
    LINK_HOW_TO_REQUEST_RR_API = (By.CSS_SELECTOR, 'a[href="#how"]')
    SECTION_R_CONCEPTS = (By.XPATH, "//*[@id='concept']")
    TITLE_ROAD_RISK = (By.CSS_SELECTOR, '.breadcrumb-title')
    LINK_LIST_OF_NATIONAL = (By.CSS_SELECTOR, "a[href$='listsource']")
    TITLE_LIST_OF_NATIONAL = (By.XPATH, "//*[@id='listsource']/h3")
    LINK_API_KEY_TAB = (By.CSS_SELECTOR, "td a[target='_blank']")
    LIST_API_KEYS = (By.CSS_SELECTOR, '.active')
    BLOCK_LIST_SOURCE = (By.XPATH, '//*[@id="listsource"]/table')


class ClimateForecastLocators:
    URL_FORCAST30 = 'https://openweathermap.org/api/forecast30'
    TITLE_FORCAST30 = (By.CSS_SELECTOR, '.col-sm-7 .breadcrumb-title')
    LINK_HOW_TO_MAKE = (By.CSS_SELECTOR, "a[href$='geo-year']")
    TITLE_HOW_TO_MAKE = (By.XPATH, '//*[@id="geo-year"]/h3')


class FooterLocators:
    FOOTER_COPYRIGHT = (By.XPATH, "//div[@class='horizontal-section my-5']/div[1]")


class MigratePageLocators:
    SUBSCRIBE_FOR_FREE_LINK = (By.XPATH, "//a[contains(@ href, '/home/sign_up')]")


class SubscriptionLocators:
    BUTTON_CONTINUE_TO_PAYMENT = (By.XPATH, "//input[@value='Continue to payment']")
    RADIOBUTTON_ORGANISATIONS = (By.XPATH, "//span[2]//input[@type='radio']")
    ERROR_MESSAGE = (By.XPATH, "//span[@class='help-block']")
    INPUT_EMAIL = (By.XPATH, "//input[@type='email']")
    INPUT_ORGANISATION = (By.XPATH, "//input[@id='unauth_subscription_form_organisation']")
    INPUT_ADDRESS_1 = (By.XPATH, "//input[@id='unauth_subscription_form_address_line_1']")
    INPUT_CITY = (By.XPATH, "//input[@id='unauth_subscription_form_city']")
    INPUT_POSTCODE = (By.XPATH, "//input[@id='unauth_subscription_form_postal_code']")
    INPUT_PHONE_NUMBER = (By.XPATH, "//input[@id='unauth_subscription_form_phone']")
    BUTTON_PAYMENT_PAGE = (By.XPATH, "//div[@class='SubmitButton-IconContainer']")
    LOADING = (By.CSS_SELECTOR, "div.LOADING-container.LOADING-double")
    LOAD_PAGE = (By.XPATH, "//div[@class='wrapper']")
    ELEMENT_STRIPE = (By.CSS_SELECTOR, "#stripe-title")


class FAQPageLocators:
    FAQ_QUESTIONS_HEADINGS = (By.CSS_SELECTOR, ".question-heading")
    FAQ_QUESTIONS_AREA = (By.CSS_SELECTOR, ".question.visible")
    FAQ_ANSWER_SECTIONS = (By.XPATH, "./following-sibling::div[@class='question-content']")
    FAQ_ANSWER_TEXT = (By.CSS_SELECTOR, "p")


class OurInitiativesPageLocators:
    INITIATIVES = By.CSS_SELECTOR, "ul[id='first-level-nav'] li:nth-child(7) a:nth-child(1)"
    SECTION = By.XPATH, "//span[contains(text(), '{}')]"
    EDUCATION_LEARN_MORE = By.CSS_SELECTOR, ".ow-btn.round.btn-black"
    QUESTION_XPATH = "//*[@id='faq']/div[{i}]/p"
    DISPLAYED_TITLE = (By.XPATH, '//div[2]//h1')
    BUTTON_LEARN_MORE = (By.CSS_SELECTOR, 'a[class="ow-btn round btn-black"]')


class ForBusinessPageLocators:
    FOR_BUSINESS = By.CSS_SELECTOR, "div[id='desktop-menu'] a[class='marketplace']"
    PRODUCTS_IN_HEADER = By.CSS_SELECTOR, "a[href='/products']"
    PRODUCTS_HEADINGS = By.CSS_SELECTOR, "a big"
    BLACK_BUTTONS = By.CSS_SELECTOR, "a[class='ow-btn round btn-black']"
    ORANGE_BUTTONS = By.CSS_SELECTOR, "a[class='btn_block orange round']"
    TALK_TO_US_BUTTON = By.XPATH, "(//a[contains(text(), 'Talk to us')])[1]"
    CURRENT_AND_FORECASTS = By.XPATH, "(//a[@class='stats white-text'])[1]"
    HISTORICAL_DATA = By.XPATH, "(//a[@class='stats white-text'])[2]"
    WEATHER_ALERTS = By.XPATH, "(//a[@class='stats white-text'])[3]"
    WEATHER_MAPS = By.XPATH, "(//a[@class='stats white-text'])[4]"
    ENERGY_PREDICTION = By.XPATH, "(//a[@class='stats white-text'])[5]"

class SearchResultPageLocators:
    ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#forecast_list_ul .alert.alert-warning")
    STRING_ENTERED_CITY = (By.CSS_SELECTOR, "#search_str")
    NOTIFICATION_PANE = (By.ID, 'forecast_list_ul')
    NOTIFICATION_BUTTON = (By.CSS_SELECTOR, '.alert.alert-warning a.close')


class CookiesSettingsPageLocators:
    RADIO_BUTTON_1 = (By.XPATH, '(//div/input)[1]')
    RADIO_BUTTON_2 = (By.XPATH, '(//div/input)[2]')
    RADIO_BUTTON_3 = (By.XPATH, '(//div/input)[3]')
    RADIO_BUTTON_4 = (By.XPATH, '(//div/input)[4]')
    LEARN_MORE_COOKIES = (By.CSS_SELECTOR, "a[href='/cookies-details']")
    SAVE_CHANGES_BUTTON = (By.XPATH, "//*[contains(text(), 'Save')]")


class MembersLocators:
    CONTINUE_TO_PAYMENT_BUTTON = (By.CSS_SELECTOR, 'input[value ="Continue to payment"]')
    CANT_BE_BLANK = (By.CSS_SELECTOR, '.help-block')
