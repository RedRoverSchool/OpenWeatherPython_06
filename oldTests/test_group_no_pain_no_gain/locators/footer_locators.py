from selenium.webdriver.common.by import By


class FooterLocators:
    ALLOW_ALL_COOKIES_LOCATOR = (By.XPATH, '//*[contains(text(), "Allow all")]')
    ASK_A_QUESTION_LINK = (By.XPATH, "(//*[contains(text(),'question')])[3]")
    MANAGE_COOKIES = (By.XPATH, "//*[contains(text(), 'Manage cookies')]")
    WEATHER_MAPS = (By.CSS_SELECTOR, 'a[href="/api#maps"]')
    BLOG_LINK = (By.XPATH, "//a[@href='https://openweather.co.uk/blog/category/weather']")