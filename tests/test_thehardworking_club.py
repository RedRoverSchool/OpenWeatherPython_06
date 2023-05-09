from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://openweathermap.org/widgets-constructor'
api_key = (By.XPATH, "//input[@id='api-key']")
city_name = (By.CSS_SELECTOR, "#city-name")
type_widget_1 = (By.XPATH, '//img[contains(@src, "themes/openweathermap/assets/vendor/owm/img/widgets/type-brown.png")]')
left_bottom_widget = (By.XPATH, '//div/*[@class="widget-left-menu widget-left-menu--brown"]')
widget_choose = (By.XPATH, "//li[@class = 'widget-choose__item']")
XPATH_CITY_NAME = (By.XPATH, "//input[@id='city-name']")
XPATH_SEARCH_FIELD_BUTTON = (By.XPATH, '//*[@id="search-city"]/i')
XPATH_FIRST_BOTTOM_WIDGET_WINDOW = (By.XPATH, '//*[@id="container-openweathermap-widget-11"]/div/div[1]/div/h2')


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


def test_TC_001_09_08_select_the_specific_city(driver, wait):
    driver.get(URL)
    search_field = driver.find_element(*XPATH_CITY_NAME)
    search_field.clear()
    search_field.click()
    search_field.send_keys("Foster city")
    search_field_button = driver.find_element(*XPATH_SEARCH_FIELD_BUTTON)
    search_field_button.click()
    wait = WebDriverWait(driver, 10)
    is_present = wait.until(EC.text_to_be_present_in_element(XPATH_FIRST_BOTTOM_WIDGET_WINDOW, 'Foster City'))
    assert is_present
