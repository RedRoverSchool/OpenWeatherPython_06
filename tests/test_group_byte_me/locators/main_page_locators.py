from selenium.webdriver.common.by import By


class MainPageLocators:
    WEATHER_IN_YOUR_CITY_FLD = (By.CSS_SELECTOR, "#desktop-menu input:nth-child(1)")
    REQUESTED_CITY = 'London, GB'
    DISPLAYED_CITY = (By.XPATH, "//*[@Class='table']//tr[1]//b/a")