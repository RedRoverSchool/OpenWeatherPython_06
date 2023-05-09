from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://openweathermap.org/widgets-constructor'
URL_2 = 'https://openweathermap.org/guide'

api_key = (By.XPATH, "//input[@id='api-key']")
city_name = (By.CSS_SELECTOR, "#city-name")
type_widget_1 = (By.XPATH, '//img[contains(@src, "themes/openweathermap/assets/vendor/owm/img/widgets/type-brown.png")]')
left_bottom_widget = (By.XPATH, '//div/*[@class="widget-left-menu widget-left-menu--brown"]')
widget_choose = (By.XPATH, "//li[@class = 'widget-choose__item']")

SOLAR = (By.CSS_SELECTOR, "li a[href*='solar-energy-prediction']")
GLOBAL_WEATHER = (By.CSS_SELECTOR, "li a[href*='push-weather-alerts']")
ROAD_RISK = (By.CSS_SELECTOR, "li a[href*='road-risk']")
GLOBAL_PRECIP = (By.CSS_SELECTOR, "li a[href*='global-precipitation-map-forecast']")
WEATHER_MAPS = (By.CSS_SELECTOR, "li a[href*='weather-map-1h']")

def test_TC_001_09_04_YourAPIKey_YourCityName_fields_visible(driver):
    driver.get(URL)
    your_api_key = driver.find_element(*api_key)
    your_city_name = driver.find_element(*city_name)
    assert your_api_key.is_displayed() and your_city_name.is_displayed()


def test_TC_001_09_07_verify_display_of_bottom_widget_1_for_selected_type(driver):
    driver.get(URL)
    driver.find_element(*type_widget_1).click()
    left_bottom_widget_appeared = (WebDriverWait(driver, 10).until(EC.presence_of_element_located(left_bottom_widget)))
    assert left_bottom_widget_appeared.is_displayed()


def test_TC_001_09_02_Verify_that_3_widgets_are_displayed(driver, wait):
    driver.get(URL)
    widget_choose_item = driver.find_elements(*widget_choose)
    for widget in widget_choose_item:
        assert widget.is_displayed(), "Some widget is not displayed"

def test_TC_004_03_01_all_links_are_visibility(driver):
    driver.get(URL_2)
    link_text_list = [
        driver.find_element(*SOLAR),
        driver.find_element(*GLOBAL_WEATHER),
        driver.find_element(*ROAD_RISK),
        driver.find_element(*GLOBAL_PRECIP),
        driver.find_element(*WEATHER_MAPS)
    ]
    for link_text in link_text_list:
        assert link_text.is_displayed()

