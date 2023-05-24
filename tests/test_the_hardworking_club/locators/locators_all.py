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
    FAHRENHEIT_BUTTON = (By.CSS_SELECTOR, 'span#imperial')

class PricePageLocators():

    SUBSCRIBE_BUTTON = (By.XPATH, '//center/a[@class="ow-btn round btn-orange"]')
    COOKIE_BUTTON = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')

    
class MainPageLocators():
  
    XPATH_PRIVACY_POLICY_BUTTON = (By.XPATH, '//*[@id="footer-website"]/div/div[2]/div[2]/div/ul/li[2]/a')


class WeatherDashboardLocators:

    CONTACT_US = (By.CSS_SELECTOR, 'div.row p.below a.btn_like')
    FOOTER_PANEL = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')

class GuidePageLocators:

    SOLAR = (By.CSS_SELECTOR, "li a[href*='solar-energy-prediction']")
    GLOBAL_WEATHER = (By.CSS_SELECTOR, "li a[href*='push-weather-alerts']")
    ROAD_RISK = (By.CSS_SELECTOR, "li a[href*='road-risk']")
    GLOBAL_PRECIP = (By.CSS_SELECTOR, "li a[href*='global-precipitation-map-forecast']")
    WEATHER_MAPS = (By.CSS_SELECTOR, "li a[href*='weather-map-1h']")

