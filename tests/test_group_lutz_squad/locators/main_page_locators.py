from selenium.webdriver.common.by import By


class MainPageLocators:
    search_city_field_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_button_locator = (By.CSS_SELECTOR, "button[class='button-round dark']")
    search_option_locator = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    displayed_city_locator = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
    no_results_notification = (By.CSS_SELECTOR, '.widget-notification > span')
    ABOUT_US_LOCATOR = (By.XPATH, "//*[text()='About us']")
