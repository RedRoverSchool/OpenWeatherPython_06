from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


URL_SOLAR_API = "https://openweathermap.org/api/solar-energy-prediction"
cities = ['New York', 'Los Angeles', 'Paris']
search_city_field_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button_locator = (By.CSS_SELECTOR, "button[class ='button-round dark']")
search_1st_option_locator = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')
loading_screen_locator = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
c_temp_locator = (By.CSS_SELECTOR, '.switch-container .option:nth-child(2)')
line_in_8_days_forecast_locator = (By.XPATH, "//div[@class='day-list-values']/div/span[contains(text(), '°C')]")
product_concept_title_locator = (By.CSS_SELECTOR, "#concept h2")
line_in_8_days_forecast_locator = (By.XPATH, "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])")
subscription_module_button = (By.CSS_SELECTOR, ".inner-footer-container div:first-of-type "
                                               ".footer-section:nth-child(2) p.section-heading")
quality_info_page = "https://openweathermap.org/accuracy-and-quality"
nwp_model = (By.CSS_SELECTOR, ".col-sm-12 > ul:first-of-type")
CONTINUE_TO_PAYMENT_BUTTON = (By.CSS_SELECTOR, 'input[value ="Continue to payment"]')
CANT_BE_BLANK = (By.CSS_SELECTOR, '.help-block')
EXPECTED_NUMBER_OF_FIELDS = 7
URL_SUBSCRIPTION_BASE = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/onecall_30/base'
MAIN_LOGO = (By.CSS_SELECTOR, 'img[src="/themes/openweathermap/assets/img/logo_white_cropped.png"]')
OUR_INITIATIVES_PAGE = 'https://openweathermap.org/our-initiatives'
MAIN_PAGE = 'https://openweathermap.org/'



@pytest.mark.parametrize('city', cities)
def test_TC_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(driver, open_and_load_main_page, city):
    search_city_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(search_city_field_locator))
    search_city_field.send_keys(city)
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    search_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(search_1st_option_locator))
    search_option.click()
    c_temp = driver.find_element(*c_temp_locator)
    c_temp.click()
    lines = driver.find_elements(*line_in_8_days_forecast_locator)
    for line in lines:
        assert line.is_displayed()


def test_TC_005_10_02_visibility_of_Product_concept_article_title(driver):
    driver.get(URL_SOLAR_API)
    product_concept_title = driver.find_element(*product_concept_title_locator)
    assert product_concept_title.is_displayed()



def test_TC_003_05_01_subscription_module_title_displayed(driver, open_and_load_main_page):
    subscription_title = driver.find_element(*subscription_module_button)
    driver.execute_script("arguments[0].click();", subscription_title)
    assert subscription_title.is_displayed()



def test_001_017_01_visibility_of_nwp_block(driver):
    driver.get(quality_info_page)
    nwp = driver.find_element(*nwp_model)
    assert nwp.is_displayed()


def test_TC_018_01_02_Verify_error_messages_for_empty_required_fields(driver):
    driver.get(URL_SUBSCRIPTION_BASE)
    driver.find_element(*CONTINUE_TO_PAYMENT_BUTTON).click()
    error_messages = driver.find_elements(*CANT_BE_BLANK)
    checks = 0
    for i in error_messages:
        assert i.is_displayed()
        checks += 1
    assert checks == EXPECTED_NUMBER_OF_FIELDS

def test_002_01_11_verify_main_logo(driver):
    driver.get(OUR_INITIATIVES_PAGE)
    m_logo = driver.find_element(*MAIN_LOGO)
    m_logo.click()
    response = requests.get(MAIN_PAGE)
    assert response.status_code == 200


