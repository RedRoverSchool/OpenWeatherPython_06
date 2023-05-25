import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# URLs
URL_guide = 'https://openweathermap.org/guide'
URL_forecast = 'https://openweathermap.org/forecast16'
URL_WEATHER_API = 'https://openweathermap.org/api'
URL_forecast30 = 'https://openweathermap.org/api/forecast30'

# Locators
how_to_start_link = (By.XPATH, "//a[contains(text(),'‘How to start and operate with API more efficientl')]")
call_16_day_daily_forecast_data = (By.XPATH, "//a[@href='#16days']")
call_16_day_daily_forecast_data_section = (By.XPATH, "(//div/section/h2)[1]")
weather_fields_api = (By.CSS_SELECTOR, "a[href='#parameter']")
other_features_link = (By.XPATH, "//a[normalize-space()='Other features']")
other_features = (By.XPATH, "//h2[normalize-space()='Other features']")
how_to_start_link_1 = (By.CSS_SELECTOR, "section[id='pro'] p[class='lead'] a")
sign_up_link = (By.CSS_SELECTOR, "a[href='/home/sign_up']")
learn_more_link = (By.XPATH, "//a[normalize-space()='Learn more']")
api_doc_button = (By.XPATH, "//section[@id='current']//div[2]//div[1]//a[1]")
subscribe_button = (By.XPATH, "//section[@id='current']//div[2]//div[1]//a[2]")

def test_TC_005_05_01_visibility_and_clickability_call_16_day_dailyforecast_data_link(driver):
    driver.get(URL_forecast)
    element = driver.find_element(*call_16_day_daily_forecast_data)
    assert element.is_displayed() and element.is_enabled()

def test_TC_004_04_01_verify_visibility_and_clickability_of_the_link(driver):
    driver.get(URL_guide)
    element = driver.find_element(*how_to_start_link)
    assert element.is_enabled() and element.is_displayed()

def test_AT_005_05_07_weatherAPI_Daily_forecast_16_days_Visibility_and_clickability(driver):
    driver.get(URL_forecast)
    element = driver.find_element(*weather_fields_api)
    assert element.is_displayed() and element.is_enabled()

def test_TC_005_06_03_redirect_to_other_features_section(driver):
    driver.get(URL_forecast30)
    driver.find_element(*other_features_link).click()
    section_title = driver.find_element(*other_features)
    assert section_title.is_displayed(), 'Title Not Found'

def test_TC_005_04_06_verify_how_to_start_link_is_visible_and_clickable(driver, wait):
    driver.get(URL_WEATHER_API)
    how_to_start = wait.until(EC.element_to_be_clickable(how_to_start_link_1))
    assert how_to_start.is_displayed() and how_to_start.is_enabled(), \
        "The 'How to start' link is not displayed on the page or is not clickable"

def test_TC_005_04_07_verify_sign_up_link_is_visible_and_clickable(driver, wait):
    driver.get(URL_WEATHER_API)
    sign_up = wait.until(EC.element_to_be_clickable(sign_up_link))
    assert sign_up.is_displayed() and sign_up.is_enabled(), \
        "The 'Sign up' link is not displayed on the page or is not clickable"

def test_TC_005_04_08_verify_learn_more_link_is_visible_and_clickable(driver, wait):
    driver.get(URL_WEATHER_API)
    learn_more = wait.until(EC.element_to_be_clickable(learn_more_link))
    assert learn_more.is_displayed() and learn_more.is_enabled(), \
        "The 'Learn more' link is not displayed on the page or is not clickable"

def test_TC_005_04_09_verify_api_doc_btn_is_visible_and_clickable(driver):
    driver.get(URL_WEATHER_API)
    api_doc = driver.find_element(*api_doc_button)
    assert api_doc.is_displayed() and api_doc.is_enabled()

def test_TC_005_04_10_verify_subscribe_button_is_visible_and_clickable(driver):
    driver.get(URL_WEATHER_API)
    subscribe_btn = driver.find_element(*subscribe_button)
    assert subscribe_btn.is_displayed() and subscribe_btn.is_enabled()

# def test_TC_005_04_11_verify_how_to_start_link_redirecting(driver):
#     driver.get(URL_WEATHER_API)
#     driver.find_element(*how_to_start_link_1).click()
#     assert driver.current_url == 'https://openweathermap.org/appid/'

def test_TC_005_05_02_redirect_to_call_16_section_title(driver):
    driver.get(URL_forecast)
    driver.find_element(*call_16_day_daily_forecast_data).click()
    call_16_section_title = driver.find_element(*call_16_day_daily_forecast_data_section)
    assert call_16_section_title.is_displayed(), 'Title "Call 16 day / daily forecast data" Not Found'
