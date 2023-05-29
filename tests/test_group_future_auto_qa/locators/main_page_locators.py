from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_SEARCH_FIELD = (By.NAME, "q")
    HEADER_SEARCH_PLACEHOLDER = (By.CSS_SELECTOR, 'input[name="q"]::placeholder')
    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    SUPPORT_MENU = (By.CSS_SELECTOR, '#support-dropdown')
    SUPPORT_FAQ_SUBMENU = (By.CSS_SELECTOR, '#support-dropdown-menu > li:nth-child(1) > a[href="/faq"]')
    SUPPORT_HOW_TO_START_SUBMENU = (By.CSS_SELECTOR, '#support-dropdown-menu > li:nth-child(2) > a[href="/appid"]')
    SUPPORT_ASK_A_QUESTION_SUBMENU = (By.CSS_SELECTOR, '#support-dropdown-menu > li:nth-child(2) > a[href*="questions"]')
    HEADER = (By.CSS_SELECTOR, 'h1')
    FOOTER_BLOG_LINK = (By.CSS_SELECTOR, ".not-foldable > .section-content > ul > :nth-child(2) > a")
    FOOTER_WIDGETS = (By.XPATH, "//a[contains(text(), 'Widgets')]")
    FOOTER_TERMS_AND_CONDITIONS_OF_SALE = (By.XPATH, "//a[normalize-space()='Terms and conditions of sale']")
    FOOTER_TERMS_AND_CONDITIONS_TITLE = (By.CSS_SELECTOR, ":nth-child(2) > :nth-child(2) > .section-heading")
    FOOTER_WEBSITE_TERMS_AND_CONDITIONS = (By.XPATH, "//a[normalize-space()='Website terms and conditions']")
    FOOTER_CURRENT_AND_FORECAST_APIS = (By.XPATH, "//a[contains(text(), 'Current and Forecast')]")
    FOOTER_HISTORICAL_WEATHER_DATA = (By.XPATH, "//a[contains(text(), 'Historical Weather Data')]")
    FOOTER_WEATHER_MAPS = (By.XPATH, "//a[contains(text(), 'Weather Maps')]")
    FOOTER_WEATHER_DASHBOARD = (By.XPATH, "//a[contains(text(), 'Weather Dashboard')]")
    product_collection = [FOOTER_CURRENT_AND_FORECAST_APIS, FOOTER_HISTORICAL_WEATHER_DATA, FOOTER_WEATHER_MAPS,
                          FOOTER_WEATHER_DASHBOARD, FOOTER_WIDGETS]
