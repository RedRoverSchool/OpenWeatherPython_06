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
    FOOTER_WIDGETS = (By.XPATH, "//a[contains(text(), 'Widgets')]")
