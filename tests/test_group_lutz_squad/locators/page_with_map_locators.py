from selenium.webdriver.common.by import By


class PageWithMapLocators:
    PAGE_WITH_MAP_LINK = 'https://openweathermap.org/weathermap'
    PAGE_WITH_MAP_PRESSURE_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[for="Pressure"]')
