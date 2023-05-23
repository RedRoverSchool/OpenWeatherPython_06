from selenium.webdriver.common.by import By


class WidgetsPageLocators():

    #
    # API_KEY = (By.XPATH, "//input[@id='api-key']")
    # CITY_NAME = (By.CSS_SELECTOR, "#city-name")

    INPUT_FIELDS = (By.CSS_SELECTOR, '.form-control')
    TYPE_WIDGET_1 = (
        By.XPATH, '//img[contains(@src, "themes/openweathermap/assets/vendor/owm/img/widgets/type-brown.png")]')
    LEFT_BOTTOM_WIDGET = (By.XPATH, '//div/*[@class="widget-left-menu widget-left-menu--brown"]')
    XPATH_CITY_NAME = (By.XPATH, "//input[@id='city-name']")
    XPATH_SEARCH_FIELD_BUTTON = (By.XPATH, '//*[@id="search-city"]/i')
    XPATH_FIRST_BOTTOM_WIDGET_WINDOW = (By.XPATH, '//*[@id="container-openweathermap-widget-11"]/div/div[1]/div/h2')
    WIDGET_CHOOSE = (By.XPATH, "//li[@class = 'widget-choose__item']")
    SUBTITLE_HEADLINE = (By.XPATH, "//h2[@class='headline first-child text-color']")



class PricePageLocators():

    SUBSCRIBE_BUTTON = (By.XPATH, '//center/a[@class="ow-btn round btn-orange"]')
    COOKIE_BUTTON = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')


