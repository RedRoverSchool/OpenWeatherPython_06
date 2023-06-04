from selenium.webdriver.common.by import By

class EightDayForecast:
    URL = 'https://openweathermap.org'
    SEARCH_SKY_IN_WORDS = (By.XPATH, "//div[@class='day-list-values']/span[contains(@class,'sub')]")


class FooterBlockLocators:
    COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
    HOW_TO_START_LINK = (By.CSS_SELECTOR, "div.section-content ul>li>a[href='/appid']")

class MainPageLocators:
    ALLOW_ALL_COOKIES_BUTTON = (By.XPATH, "//button[@class ='stick-footer-panel__link']")
    ABOUT_US_BUTTON = (By.XPATH, "//a[@href='/about-us']")
class AboutUsPageLocators():
    HEADER = (By.XPATH, "//h1")