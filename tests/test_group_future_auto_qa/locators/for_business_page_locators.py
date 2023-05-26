from selenium.webdriver.common.by import By


class ForBusinessPageLocators:
    FOR_BUSINESS_PAGE_URL = "https://openweather.co.uk/"
    FOR_BUSINESS = By.CSS_SELECTOR, "div[id='desktop-menu'] a[class='marketplace']"
    PRODUCTS_IN_HEADER = By.CSS_SELECTOR, "a[href='/products']"
    PRODUCTS_HEADINGS = By.CSS_SELECTOR, "a big"
    BLACK_BUTTONS = By.CSS_SELECTOR, "a[class='ow-btn round btn-black']"
    ORANGE_BUTTONS = By.CSS_SELECTOR, "a[class='btn_block orange round']"

