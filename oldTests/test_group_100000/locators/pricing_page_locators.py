from selenium.webdriver.common.by import By


class PricingLocators:
    URL_PRICING = 'https://openweathermap.org/price'
    LINK_TEXT_ONE_CALL = (By.CSS_SELECTOR, "#onecall > div > div > h2")
