from selenium.webdriver.common.by import By


class MainLocator:
    TO_IMPERIAL_BTN = By.XPATH, "//div[contains(text(),'Imperial: °F, mph')]"
    TO_METRIC_BTN = By.XPATH, "//div[contains(text(),'Metric: °C, m/s')]"
    INITIATIVES = By.CSS_SELECTOR, "ul[id='first-level-nav'] li:nth-child(7) a:nth-child(1)"
    sections = ["Education", "Healthcare", "Open Source", "Weather stations"]
    section_locator = lambda section: (By.XPATH, f"//span[contains(text(), '{section}')]")
    QUESTION_XPATH = "//*[@id='faq']/div[{i}]/p"
    EDUCATION_SECTION_PAGE = "https://openweathermap.org/our-initiatives/student-initiative"
    EDUCATION_LEARN_MORE = By.CSS_SELECTOR, ".ow-btn.round.btn-black"
    LOADER_CONTAINER = By.CSS_SELECTOR, 'div.owm-loader-container > div'
    SEARCH_CITY_INPUT = By.CSS_SELECTOR, "input[placeholder='Search city']"
    BTN_SEARCH = By.CSS_SELECTOR, "button[class ='button-round dark']"
    SEARCH_DROPDOWN_MENU = By.CLASS_NAME, 'search-dropdown-menu'
    DROPDOWN_LIST = By.CSS_SELECTOR, 'ul.search-dropdown-menu li'
    SEARCH_DROPDOWN_MENU_FIRST_CHILD = By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)'
    SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT = By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'
    MODULE_DOWNLOAD_OPENWEATHER_APP = (By.XPATH, "//div[@class='my-5']/p")
    FIRST_DAY_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'ul.day-list li:nth-child(1) span:nth-child(1)'
    LIST_DAYS_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'div .day-list'
    DAYS_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'div .day-list li'
    APP_STORE_BRAND_LINK = By.CSS_SELECTOR, "img[src='/themes/openweathermap/assets/img/mobile_app/app-store-badge.svg']"
    GOOGLE_PLAY_BRAND_LINK = By.CSS_SELECTOR, "img[alt='Get it on Google Play']"



