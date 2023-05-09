from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://openweathermap.org/widgets-constructor'
URL_1 = 'https://openweathermap.org/weather-dashboard'
CONTACT_US = (By.CSS_SELECTOR, 'div.row p.below a.btn_like')
FITTER_PANEL = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')
api_key = (By.XPATH, "//input[@id='api-key']")
city_name = (By.CSS_SELECTOR, "#city-name")
type_widget_1 = (By.XPATH, '//img[contains(@src, "themes/openweathermap/assets/vendor/owm/img/widgets/type-brown.png")]')
left_bottom_widget = (By.XPATH, '//div/*[@class="widget-left-menu widget-left-menu--brown"]')
widget_choose = (By.XPATH, "//li[@class = 'widget-choose__item']")

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


def test_TC_006_05_03_button_Contact_Us_works(driver):

    driver.get(URL_1)
    my_CONTACT_US = driver.find_element(*CONTACT_US)
    assert my_CONTACT_US.is_enabled()

