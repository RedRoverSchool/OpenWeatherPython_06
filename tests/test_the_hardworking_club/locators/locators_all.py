from selenium.webdriver.common.by import By


class WidgetsPageLocators():

    #
    # API_KEY = (By.XPATH, "//input[@id='api-key']")
    # CITY_NAME = (By.CSS_SELECTOR, "#city-name")

    INPUT_FIELDS = (By.CSS_SELECTOR, '.form-control')
    TYPE_WIDGET_1 = (
        By.XPATH, '//img[contains(@src, "themes/openweathermap/assets/vendor/owm/img/widgets/type-brown.png")]')
    LEFT_BOTTOM_WIDGET = (By.XPATH, '//div/*[@class="widget-left-menu widget-left-menu--brown"]')



