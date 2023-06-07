from selenium.webdriver.common.by import By

class EightDayForecast:
    URL = 'https://openweathermap.org'
    SEARCH_SKY_IN_WORDS = (By.XPATH, "//div[@class='day-list-values']/span[contains(@class,'sub')]")


class FooterBlockLocators:
    HOW_TO_START_LINK = (By.CSS_SELECTOR, "div.section-content ul>li>a[href='/appid']")

class MainPageLocators:
    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    MANAGE_COOKIES_BTN = (By.XPATH, '//*[@id="stick-footer-panel"]//a')
