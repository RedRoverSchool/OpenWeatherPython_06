from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = 'https://openweathermap.org/'
    search_city_field_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_button_locator = (By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_dropdown_option = (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")
    GRAPHIC_HOURLY_FORECAST_LOCATOR = (By.CSS_SELECTOR, "canvas[id=chart-component]")
    WEATHER_ITEMS_LOCATOR = (By.CSS_SELECTOR, "ul.weather-items")
    WEATHER_ITEM_LOCATOR = (By.CSS_SELECTOR, 'ul.weather-items li:nth-child(1)')

