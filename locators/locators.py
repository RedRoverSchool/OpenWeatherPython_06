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
    HEADER_SEARCH_FIELD = (By.NAME, "q")


class DashboardPageLocators:
    pass


class PricingPageLocators:
    pass


class ApiPageLocators:
    pass

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
