from selenium.webdriver.common.by import By


class RoadRiskApi:
    ROAD_RISK_API_LINK = 'https://openweathermap.org/api/road-risk'
    TITLE_HOW_TO_RR_API = (By.XPATH, "//*[@id='how']/h2")
    LINK_HOW_TO_REQUEST_RR_API = (By.CSS_SELECTOR, 'a[href="#how"]')
    SECTION_R_CONCEPTS = (By.XPATH, "//*[@id='concept']")
    TITLE_ROAD_RISK = (By.CSS_SELECTOR, '.breadcrumb-title')
    LINK_LIST_OF_NATIONAL = (By.CSS_SELECTOR, "a[href$='listsource']")
    TITLE_LIST_OF_NATIONAL = (By.XPATH, "//*[@id='listsource']/h3")


class WeatherConditions:
    DRIZZLE_LOCATOR = (By.XPATH, '//a[contains(@href, "#Drizzle")]/ancestor-or-self::table')
    CONDITION_URL = 'https://openweathermap.org/weather-conditions'