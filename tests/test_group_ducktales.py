from selenium.webdriver import Keys
import pytest
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import random
import string

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

#Экспериментальный тест с проверкой температуры. Тестирование рекомендовано провести для нескольких географических точек, сильно разнящихся по климату
def test_city_temperature(driver):
    driver.get('http://openweathermap.org/')
    time.sleep(10)
    temperature_scale_choice = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(text(), 'Metric: °C, m/s')]")))  # удостоверимся, что шкала для теста - Цельсий (можно рассматривать это как precondition, но лучше подстраховаться)
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
    assert displayed_city.text == expected_city #проверяем, соответствует ли вывод запросу
    displayed_temperature = WebDriverWait(driver, 15).until(EC.presence_of_element_located( #проверяем, адекватны ли температурные значения
        (By.CSS_SELECTOR, "span[class='heading']")))
    displayed_temperature_text = displayed_temperature.text
    import re
    x = re.compile(r"^(-?[0-9]+)°C$")
    temperature = int(x.match(displayed_temperature_text).group(1))
    assert -10 <= temperature <= 10  # граничные значения исходя из средних температур сезона за всю историю наблюдений


def test_new_pass():
    pass

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pytest

TO_IMPERIAL_BTN = By.XPATH, "//div[contains(text(),'Imperial: °F, mph')]"
TO_METRIC_BTN = By.XPATH, "//div[contains(text(),'Metric: °C, m/s')]"
INITIATIVES = By.CSS_SELECTOR, "ul[id='first-level-nav'] li:nth-child(7) a:nth-child(1)"
sections = ["Education", "Healthcare", "Open Source", "Weather stations"]
LOADER_CONTAINER = By.CSS_SELECTOR, 'div.owm-loader-container > div'
SEARCH_CITY_INPUT = By.CSS_SELECTOR, "input[placeholder='Search city']"
BTN_SEARCH = By.CSS_SELECTOR, "button[class ='button-round dark']"
SEARCH_DROPDOWN_MENU = By.CLASS_NAME, 'search-dropdown-menu'
SEARCH_DROPDOWN_MENU_FIRST_CHILD = By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)'
SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT = By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'
MODULE_DOWNLOAD_OPENWEATHER_APP = By.XPATH, "//div[@class='my-5']/p"
FIRST_DAY_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'ul.day-list li:nth-child(1) span:nth-child(1)'

WEEKDAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')


def test_tc_001_01_01_verify_city_name_displayed_by_zip(driver, open_and_load_main_page, wait):
    search_city_field = driver.find_element(*SEARCH_CITY_INPUT)
    search_city_field.send_keys('66002')
    search_button = driver.find_element(*BTN_SEARCH)
    search_button.click()
    search_option = wait.until(EC.element_to_be_clickable(SEARCH_DROPDOWN_MENU_FIRST_CHILD))
    search_option.click()
    expected_city = 'Atchison, US'
    wait.until(EC.text_to_be_present_in_element(SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT, 'Atchison'))
    displayed_city = driver.find_element(* SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT).text
    assert displayed_city == expected_city


def test_tc_001_01_02_verify_dropdown_options_contain_valid_value(driver, open_and_load_main_page, wait):
    driver.find_element(*SEARCH_CITY_INPUT).send_keys('California')
    driver.find_element(*BTN_SEARCH).click()
    wait.until(EC.element_to_be_clickable(SEARCH_DROPDOWN_MENU))
    dropdown_list = driver.find_element(*SEARCH_DROPDOWN_MENU)
    for i in dropdown_list.find_elements(By.CSS_SELECTOR, 'li'):
        assert 'California' in i.text, 'Not all search suggestions in the drop-down list contain "California"'


# TC_001.02.04_01 | Main page> Search city widget > Verify the buttons for metric and imperial are visible and clickable
def test_tc_001_02_04_01_switch_toggle_buttons(driver, open_and_load_main_page, wait):
    # switch the temperature system to imperial
    imperial_button = driver.find_element(*TO_IMPERIAL_BTN)
    imperial_button.click()
    metric_button = driver.find_element(*TO_METRIC_BTN)
    metric_button.click()
    # Verify that toggle buttons are displayed and clickable
    assert metric_button.is_displayed() and imperial_button.is_displayed()
    assert metric_button.is_enabled() and imperial_button.is_enabled()


def test_tc_003_09_01_the_module_title_display(driver, open_and_load_main_page, wait):
    expected_module_title = "Download OpenWeather app"
    module_download_openweather_app = driver.find_element(*MODULE_DOWNLOAD_OPENWEATHER_APP)
    module_download_openweather_app.location_once_scrolled_into_view
    actual_module_title = module_download_openweather_app.text
    assert actual_module_title == expected_module_title


def test_TC_001_04_03_verify_in_day_list_first_element_day_by_week(driver, open_and_load_main_page):
    day_by_weak = driver.find_element(*FIRST_DAY_IN_8_DAY_FORECAST).text[:3]
    day_by_computer = datetime.now().weekday()
    today = WEEKDAYS[day_by_computer]
    assert day_by_weak == f'{today}'


def test_tc_001_04_05_main_page_search_city_widget_8_day_forecast_first_element_number_day(driver, open_and_load_main_page):
    number_day = driver.find_element(*FIRST_DAY_IN_8_DAY_FORECAST).text[-2:]
    if number_day.startswith('0'):
        number_day = number_day[1:]
    number_day_by_computer = datetime.now().day
    assert number_day == f'{number_day_by_computer}'


def get_section_locator(section):
    return (By.XPATH, f"//span[contains(text(), '{section}')]")


@pytest.mark.parametrize("section", sections)
def test_010_01_01_01_verify_sections(driver, open_and_load_main_page, section):
    our_initiatives_link = driver.find_element(*INITIATIVES)
    our_initiatives_link.click()
    section_locator = get_section_locator(section)
    section_element = driver.find_element(*section_locator)
    assert section_element.is_displayed(), f"Section '{section}' not found on the page"

def test_TC_001_04_04_verify_in_day_list_first_element_month(driver, open_and_load_main_page):
    month = driver.find_element(*FIRST_DAY_IN_8_DAY_FORECAST).text[5:-3]
    month_by_computer = datetime.now().month
    current_month = MONTHS[month_by_computer -1]
    assert month == f'{current_month}'
