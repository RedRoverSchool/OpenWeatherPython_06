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
    ASK_A_QUESTION_OPTION = (By.XPATH, "//*[@id='support-dropdown-menu']//a[@href='https://home.openweathermap.org/questions']")


class MainPageLocators:
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
    SEARCH_DROPDOWN_OPTION = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    SEARCH_CITY_FIELD = (By.CSS_SELECTOR, "input[placeholder='Search city']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[class ='button-round dark']")
    DISPLAYED_CITY = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
    NO_RESULTS_NOTIFICATION = (By.CSS_SELECTOR, '.widget-notification > span')
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    ABOUT_US_BUTTON = (By.XPATH, "//a[@href='/about-us']")
    SEARCH_1ST_OPTION_LOCATOR = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')
    C_TEMP_LOCATOR = (By.CSS_SELECTOR, '.switch-container .option:nth-child(2)')
    LINE_IN_8_DAYS_FORECAST_LOCATOR = (By.XPATH, "//div[@class='day-list-values']/div/span[contains(text(), '°C')]")
    AGRICULTURE_ANALYTICS_TITLE_LOCATOR = (By.CSS_SELECTOR, ".section-content > .mobile-padding > div > h2")


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


class OpenAgroLocators:

    REQUEST_DATA_LOCATORS = (By.XPATH, '//a[text()="Request data"]')
    REQUEST_DATA_BUTTON = (By.CSS_SELECTOR, ".open-agro-banner__actions a")


class SolarApiLocators:

    HOW_TO_GET_ACCESS_LINK = (By.XPATH, '//a[@href="#how"]')
    HOW_TO_GET_ACCESS_TITLE = (By.CSS_SELECTOR, "#how h2")
    PRODUCT_CONCEPT_TITLE = (By.CSS_SELECTOR, "#concept h2")

