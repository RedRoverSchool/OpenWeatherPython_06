from selenium.webdriver.common.by import By


class ForBusinessPageLocators:
    FOR_BUSINESS_PAGE_URL = "https://openweather.co.uk/"
    FOR_BUSINESS = By.CSS_SELECTOR, "div[id='desktop-menu'] a[class='marketplace']"
    PRODUCTS_IN_HEADER = By.CSS_SELECTOR, "a[href='/products']"
    PRODUCTS_HEADINGS = By.CSS_SELECTOR, "a big"
    BLACK_BUTTONS = By.CSS_SELECTOR, "a[class='ow-btn round btn-black']"
    ORANGE_BUTTONS = By.CSS_SELECTOR, "a[class='btn_block orange round']"
    TALK_TO_US_BUTTON = By.XPATH, "(//a[contains(text(), 'Talk to us')])[1]"
    CURRENT_AND_FORECASTS = By.XPATH, "(//a[@class='stats white-text'])[1]"
    HISTORICAL_DATA = By.XPATH, "(//a[@class='stats white-text'])[2]"
    WEATHER_ALERTS = By.XPATH, "(//a[@class='stats white-text'])[3]"
    WEATHER_MAPS = By.XPATH, "(//a[@class='stats white-text'])[4]"
    ENERGY_PREDICTION = By.XPATH, "(//a[@class='stats white-text'])[5]"

