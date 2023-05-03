from selenium.webdriver import Keys
import pytest
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import random
import string

import requests
import re


BASE_URL = "https://openweathermap.org/"
URL_sing_in_page = "https://home.openweathermap.org/users/sign_in"
email_field = (By.ID, 'user_email')
user_email = "jtzcmspsmgvbep@bugfoo.com"
user_password = "Test1212"
password_field = (By.ID, 'user_password')
submit_button = (By.CSS_SELECTOR, '.btn-color[value="Submit"]')
tab_api_keys = (By.CSS_SELECTOR, '#myTab [href="/api_keys"')
URL_api_keys_page = 'https://home.openweathermap.org/api_keys'
SIGN_IN_ALERT = By.CLASS_NAME, 'panel-body'


def random_word():
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for _ in range(8))
    return random_word


@pytest.fixture()
def open_api_keys_page(driver):
    wait = WebDriverWait(driver, 15)
    driver.get(URL_sing_in_page)
    wait.until(EC.element_to_be_clickable(email_field)).send_keys(user_email)
    wait.until(EC.element_to_be_clickable(password_field)).send_keys(user_password)
    wait.until(EC.element_to_be_clickable(submit_button)).click()
    wait.until(EC.element_to_be_clickable(tab_api_keys)).click()


class TestSignInPage:
    def test_wrong_data_get_alert(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(URL_sing_in_page)
        wait.until(EC.element_to_be_clickable(email_field)).send_keys(random_word())
        wait.until(EC.element_to_be_clickable(password_field)).send_keys(random_word())
        wait.until(EC.element_to_be_clickable(submit_button)).click()
        assert driver.find_element(*SIGN_IN_ALERT).is_displayed(), "не отображается 'Alert Invalid...' "


def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    expected_city = 'New York City, US'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


class TestApiKeysPage:
    def test_open_my_api_keys(self, driver, open_api_keys_page):
        expected_api_keys_URL = URL_api_keys_page
        actual_url = driver.current_url
        assert actual_url == expected_api_keys_URL, 'The API page URL does not match expected'

    def test_api_keys_tab_is_active(self, driver, open_api_keys_page):
        my_tab_elements = driver.find_elements(By.CSS_SELECTOR, '#myTab li')
        expected_result = "active"
        actual_result = my_tab_elements[2].get_attribute('class')
        assert actual_result == expected_result, "API Keys tab is not active"

    def test_change_status_api_key(self, driver, open_api_keys_page):
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="edit_key_btn edit-key-btn"]')))
        first_column_values = driver.find_elements(By.XPATH, "//tbody/tr[1]/td")
        initial_status = first_column_values[2].text
        if initial_status == "Inactive":
            switch_status = first_column_values[3].find_element(By.CSS_SELECTOR, '.fa.fa-toggle-off')
            switch_status.click()
            alert = driver.switch_to.alert
            alert.accept()
        else:
            switch_status = first_column_values[3].find_element(By.CSS_SELECTOR, '.fa.fa-toggle-on')
            switch_status.click()
            alert = driver.switch_to.alert
            alert.accept()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="edit_key_btn edit-key-btn"]')))
        first_column_values_after_switch = driver.find_elements(By.XPATH, "//tbody/tr[1]/td")
        current_status = first_column_values_after_switch[2].text
        assert current_status != initial_status, "API Key status has not changed"

    def test_status_api_key_not_changed(self, driver, open_api_keys_page):
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="edit_key_btn edit-key-btn"]')))
        first_column_values = driver.find_elements(By.XPATH, "//tbody/tr[1]/td")
        initial_status = first_column_values[2].text
        if initial_status == "Inactive":
            switch_status = first_column_values[3].find_element(By.CSS_SELECTOR, '.fa.fa-toggle-off')
            switch_status.click()
            alert = driver.switch_to.alert
            alert.dismiss()
        else:
            switch_status = first_column_values[3].find_element(By.CSS_SELECTOR, '.fa.fa-toggle-on')
            switch_status.click()
            alert = driver.switch_to.alert
            alert.dismiss()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="edit_key_btn edit-key-btn"]')))
        first_column_values_after_switch = driver.find_elements(By.XPATH, "//tbody/tr[1]/td")
        current_status = first_column_values_after_switch[2].text
        assert current_status == initial_status, "API Key status was changed"

    def test_toggle_was_changed(self, driver, open_api_keys_page):
        initial_toggle_icon = driver.find_element(By.CSS_SELECTOR,
                                                  '.edit_key_btn[rel="nofollow"] i').get_attribute('class')
        toggle_icon = driver.find_element(By.CSS_SELECTOR, '.edit_key_btn[rel="nofollow"]')
        toggle_icon.click()
        alert = driver.switch_to.alert
        alert.accept()
        current_toggle_icon = driver.find_element(By.CSS_SELECTOR,
                                                  '.edit_key_btn[rel="nofollow"] i').get_attribute('class')
        assert current_toggle_icon != initial_toggle_icon, "The toggle button icon has not changed"

    def test_edit_api_key_name(self, driver, open_api_keys_page):
        wait = WebDriverWait(driver, 15)
        edit_api_key_icon = driver.find_element(By.CSS_SELECTOR, '.edit_key_btn .fa-edit')
        edit_api_key_icon.click()
        driver.switch_to.default_content()
        expected_title_api_rename_popup = 'Edit API key name'
        wait.until(
            EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR, '.pop-up-footer .button-round.dark'))))
        actual_expected_title_api_rename_popup = driver.find_element(By.CLASS_NAME, 'pop-up-header').text
        assert actual_expected_title_api_rename_popup == expected_title_api_rename_popup, \
            'The rename api key popup did not open'
        initial_api_key_name = driver.find_element(By.CSS_SELECTOR, '#new_edit_key_form .owm_input').text
        if initial_api_key_name == "New_Name_API_key":
            api_key_name_field_key_name_field = driver.find_element(By.CSS_SELECTOR, '#new_edit_key_form .owm_input')
            api_key_name_field_key_name_field.clear()
            api_key_name_field_key_name_field.send_keys("Default")
            expected_api_key_name = "Defaul"
        else:
            api_key_name_field_key_name_field = driver.find_element(By.CSS_SELECTOR, '#new_edit_key_form .owm_input')
            api_key_name_field_key_name_field.clear()
            api_key_name_field_key_name_field.send_keys("New_Name_API_key")
            expected_api_key_name = "New_Name_API_key"
        save_api_key_name_button = driver.find_element(By.CSS_SELECTOR, '.pop-up-footer .button-round.dark').click()
        actual_api_key_name = driver.find_element(By.XPATH, "//div[@class='col-md-8']//tr[1]//td[2]").text
        assert actual_api_key_name == expected_api_key_name, 'The APY key has not changed'


def test_check_page_title(driver):
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_authorization_page(driver):
    pass


def test_registration(driver):
    driver.get('https://openweathermap.org/home/sign_in')
    enter_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_email")))
    enter_email.send_keys('badlolpro@gmail.com')
    enter_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_password")))
    enter_password.send_keys('36Pv@tdm2H7/x-d')
    click_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Submit']")))
    click_submit_button.click()
    expected_message = 'Signed in successfully.'
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='panel-body']")))
    assert success_message.text == expected_message


# Экспериментальный тест с проверкой температуры. Тестирование рекомендовано провести для нескольких географических точек, сильно разнящихся по климату
def test_city_temperature(driver):
    driver.get('http://openweathermap.org/')
    time.sleep(10)
    temperature_scale_choice = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH,
         "//div[contains(text(), 'Metric: °C, m/s')]")))  # удостоверимся, что шкала для теста - Цельсий (можно рассматривать это как precondition, но лучше подстраховаться)
    temperature_scale_choice.click()
    search_city_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[placeholder='Search city']")))
    search_city_field.send_keys('Reykjavík')
    search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[class='button-round dark']")))
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//span[contains(text(), 'Reykjavík, IS')]")))
    search_option.click()
    expected_city = 'Reykjavík, IS'
    displayed_city = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(), 'Reykjavík, IS')]")))
    assert displayed_city.text == expected_city  # проверяем, соответствует ли вывод запросу
    displayed_temperature = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(  # проверяем, адекватны ли температурные значения
            (By.CSS_SELECTOR, "span[class='heading']")))
    displayed_temperature_text = displayed_temperature.text
    import re
    x = re.compile(r"^(-?[0-9]+)°C$")
    temperature = int(x.match(displayed_temperature_text).group(1))
    assert -10 <= temperature <= 10  # граничные значения исходя из средних температур сезона за всю историю наблюдений


def test_new_pass():
    pass


def test_forecast_info(driver):
    print(BASE_URL)
    driver.get(BASE_URL)
    forecast_period_head = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.daily-container.block>h3")))
    assert forecast_period_head.text == '8-day forecast'


#Тест сравнивает параметры из api и с веб-страницы
GEO_URL = 'http://api.openweathermap.org/geo/1.0/direct'
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'
WEATHER_WEB_URL = 'http://openweathermap.org/'
STATUS_OK = 200
WEATHER_API_APPID = '40b38098e34cc96139b85134c113fe3b' # ключ дается сайтом перманентно при регистрации
NAME_CITY = 'Reykjavík, IS'
PARAM_WEATHER_KEY = 'main' #тут и ниже можно подставить любой параметр и его селектор
PARAM_WEATHER_VALUE = 'temp'
SEARCH_OPTION_SELECTOR = '//span[contains(text(), "Reykjavík, IS")]'
DISPLAYED_CITY_SELECTOR = '//h2[contains(text(), "Reykjavík, IS")]'
DISPLAYED_PARAM_SELECTOR = 'span[class="heading"]'



@pytest.fixture(scope='module')
def api_geo():
    geo_params = {
        'q': NAME_CITY,
        'appid': WEATHER_API_APPID,
        'limit': 1
    }
    response_geo = requests.get(GEO_URL, params=geo_params)
    assert response_geo.status_code == STATUS_OK
    assert response_geo is not None
    response_geo_data = response_geo.json()[0]
    lat = response_geo_data['lat']
    lon = response_geo_data['lon']
    assert lat in response_geo_data.values()
    assert lon in response_geo_data.values()
    return lat, lon

@pytest.fixture()
def api_weather(api_geo):
    lat, lon = api_geo
    response_weather = requests.get(WEATHER_API_URL, {
        'lat': lat,
        'lon': lon,
        'appid': WEATHER_API_APPID,
        'units': 'metric'
    })
    assert response_weather.status_code == STATUS_OK
    assert response_weather is not None
    response_weather_data = response_weather.json()
    assert PARAM_WEATHER_KEY in response_weather_data.keys()
    return response_weather_data


@pytest.fixture()
def api_param(api_weather):
    response_weather_by_key = api_weather[PARAM_WEATHER_KEY]
    raw_param = response_weather_by_key[PARAM_WEATHER_VALUE]
    assert raw_param in response_weather_by_key.values()
    final_param = round(float(raw_param))
    return final_param

@pytest.fixture()
def web_param(driver):
    driver.get(WEATHER_WEB_URL)
    time.sleep(5)
    search_city_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[placeholder='Search city']")))
    search_city_field.send_keys(NAME_CITY)
    search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[class='button-round dark']")))
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, SEARCH_OPTION_SELECTOR)))
    search_option.click()
    expected_city = NAME_CITY
    displayed_city = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, DISPLAYED_CITY_SELECTOR)))
    assert displayed_city.text == expected_city
    temperature_scale_choice = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, '//div[contains(text(), "Metric: °C, m/s")]')))  # удостоверимся, что шкала для теста - Цельсий (можно рассматривать это как precondition, но лучше подстраховаться)
    temperature_scale_choice.click()
    displayed_param = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, DISPLAYED_PARAM_SELECTOR)))
    displayed_param1 = displayed_param.text
    pattern = re.compile(r'^([0-9]+[.]?[0-9]*)')
    final_displayed_param = round(float(pattern.match(displayed_param1).group(1)))
    return final_displayed_param

def test_matching_param(api_param, web_param):
    assert abs(web_param-api_param) <= 2
    print('Matched successfully')

