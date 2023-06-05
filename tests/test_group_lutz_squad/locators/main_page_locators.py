from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_CITY_FIELD_LOCATOR = (By.CSS_SELECTOR, "input[placeholder='Search city']")
    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[class='button-round dark']")
    SEARCH_OPTION_LOCATOR = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    DISPLAYED_CITY_LOCATOR = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
    NO_RESULTS_NOTIFICATION_LOCATOR = (By.CSS_SELECTOR, '.widget-notification > span')
    ABOUT_US_LOCATOR = (By.XPATH, "//*[text()='About us']")
