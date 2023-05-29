from selenium.webdriver.common.by import By


class GuidePageLocators:
    NWP_MODEL = (By.CSS_SELECTOR, ".col-sm-12 > ul:first-of-type")
    TITLE_NWP_MODEL_LOCATOR = (By.CSS_SELECTOR, '.col-sm-12 ol h2:nth-of-type(2)')
    HISTORICAL_COLLECTION_LINKS = (By.CSS_SELECTOR, ".col-sm-12 ol ul:nth-of-type(2) a")
    HISTORICAL_COLLECTION_MODULE = (By.CSS_SELECTOR, ".col-sm-12 ol ul:nth-of-type(2)")
    LINK_HISTORICAL_ARCHIVE = (By.PARTIAL_LINK_TEXT, "archive")
    CLICK_ALLOW_IN_STICK_FOOTER = (By.CLASS_NAME, 'stick-footer-panel__link')


class MainPageLocators:
    SEARCH_CITY_FIELD_LOCATOR = (By.CSS_SELECTOR, "input[placeholder='Search city']")
    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[class ='button-round dark']")
    SEARCH_1ST_OPTION_LOCATOR = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')
    C_TEMP_LOCATOR = (By.CSS_SELECTOR, '.switch-container .option:nth-child(2)')
    LINE_IN_8_DAYS_FORECAST_LOCATOR = (By.XPATH, "//div[@class='day-list-values']/div/span[contains(text(), '°C')]")
    AGRICULTURE_ANALYTICS_TITLE_LOCATOR = (By.CSS_SELECTOR, ".section-content > .mobile-padding > div > h2")
