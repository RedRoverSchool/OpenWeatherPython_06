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

class DashboardPageLocators:
    pass

class PricingPageLocators:
    pass

class ApiPageLocators:
    pass