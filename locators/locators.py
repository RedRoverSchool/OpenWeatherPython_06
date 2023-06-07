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

    product_collection = [CURRENT_AND_FORECAST_APIS, HISTORICAL_WEATHER_DATA_LINK, WEATHER_MAPS_LINK,
                          WEATHER_DASHBOARD_LINK, WIDGETS]

    METRIC_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
    IMPERIAL_BUTTON = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
    CURRENT_TEMP = (By.CSS_SELECTOR, "div.current-temp span.heading")
    LOC_DATE_TIME = (By.XPATH, "//div[@class='current-container mobile-padding']/div/span[@class='orange-text']")
    CITY_NAME = (By.CSS_SELECTOR, "div.current-container.mobile-padding div h2")
    LOC = (By.CSS_SELECTOR, "div.control-el svg.icon-current-location")
    LOAD_DIV = (By.CSS_SELECTOR, 'div.owm-loader-container > div')


class DashboardPageLocators:
    BTN_DASHBOARD = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
    TITLE_HOW_TO_START = (By.XPATH, "//div/h2[contains(text(),'How to Start')]")
    TRY_THE_DASHBOARD2_BTN = (By.XPATH, "//div[6]//a[text()='Try the Dashboard']")
    PANEL_SIGN_IN_FORM = (By.CSS_SELECTOR, '.col-md-6 .panel-heading')
    WEATHER_SYMBOL = (By.CSS_SELECTOR, "ul  > li:nth-child(3) > span.symbol")


class PricingPageLocators:
    URL_PRICING = 'https://openweathermap.org/price'
    LINK_TEXT_ONE_CALL = (By.CSS_SELECTOR, "#onecall > div > div > h2")


class ApiPageLocators:
    API_PAGE = 'https://openweathermap.org/api'
    button_weather_alerts_api_doc = (By.CSS_SELECTOR, "//*[@id='current']//a[@href='/api/push-weather-alerts']")


class AboutUsPageLocators:
    HEADER = (By.XPATH, "//h1")
    IMAGE_BESIDE_HEADER = (By.CSS_SELECTOR, "img.tablet-plus")
    HEADERS_ON_PAGE_FOOTER = (
        By.XPATH, "//div[@class='horizontal-section']/div[not(contains(@class,'not-foldable'))]/p")
    NEWS_AND_UPDATES_BUTTON = (By.XPATH, "// div / a[contains( @ href, 'blog/category/weather')]")
    APP_STORE_BUTTON = (By.XPATH, "//a[contains(@href, 'app/openweather')]/img")
    BYU_BY_SUBSCRIPTIONS = (By.XPATH, "//a[contains(@href, 'subscriptions')]")


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


class SignInLocator:
    EMAIL_INPUT = By.CSS_SELECTOR, '#user_email'
    PASSWORD_INPUT = By.CSS_SELECTOR, '#user_password'
    SUBMIT_BUTTON = By.CSS_SELECTOR, "input[value='Submit']"


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


class GuideLocators:
    GUIDE_URL = 'https://openweathermap.org/guide'
    guide_fast_way_links_locators = [(By.XPATH, '//*[@class="lead"]//*[@href="https://openweather.co.uk/"]'),
                                     (By.XPATH, '//p[2]//*[@href="/api"]'),
                                     (By.XPATH, '//p[2]//*[@href="/api/road-risk"]'),
                                     (By.XPATH, '//p[2]//*[@href="/api/solar-energy-prediction"]')]
    INDUSTRY_APIS_LOCATOR = (By.XPATH, "//*[contains(text(),'industry standard APIs')]")
    ONE_CALL_API_BY_CALL_LOCATOR = (By.XPATH, "//*[text()='One Call API by call']")
    SUBSCRIBE_TO_ONE_CALL_BY_CALL_BUTTON = (By.CSS_SELECTOR, "a[href='/price'].ow-btn.round.btn-orange")


class PartnersLocators:
    APACHE_CAMEL_BUTTON = (By.CSS_SELECTOR, 'a[href*="camel.apache"]')
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'Allow all')]")


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
