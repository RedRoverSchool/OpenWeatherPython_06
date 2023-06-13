from selenium.webdriver.common.by import By


class MainPageLocators:
    WEATHER_IN_YOUR_CITY_FLD = (By.CSS_SELECTOR, "#desktop-menu input:nth-child(1)")
    REQUESTED_CITY = 'London, GB'
    DISPLAYED_CITY = (By.XPATH, "//*[@Class='table']//tr[1]//b/a")
    SEARCH_CITY_FIELD_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
    SEARCH_BUTTON_Locator = (By.CSS_SELECTOR, "button[class='button-round dark']")
    SEARCH_OPTION_Locator = (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")
    DISPLAYED_CITY_1_Locator = (By.CSS_SELECTOR, ".grid-container.grid-4-5 h2")
    NO_RESULTS_NOTIFICATION = (By.CSS_SELECTOR, '.widget-notification > span')